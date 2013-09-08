# Copyright (c) 2013 gerrit-cli Developers.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
import logging
from operator import itemgetter

from cliff.lister import Lister

from gerrit import filters
from gerrit import reviews


class List(Lister):
    """Show a list of files in the current directory.

    The file name and size are printed by default.
    """

    log = logging.getLogger(__name__)

    def get_parser(self, name):
        parser = super(List, self).get_parser(name)
        parser.add_argument('host', help="Gerrit SSH host or config")
        parser.add_argument('-p', '--port', default=29418, type=int,
                            help="Gerrit SSH port")
        parser.add_argument('-l', '--limit', type=int,
                            help="Number of review to retrieve")
        parser.add_argument('--projects', nargs='+')
        return parser

    def _get_review_votes(self, patch_set):
        data = []
        approvals = patch_set.get('approvals', [])
        for ps in sorted(approvals, key=itemgetter('value')):
            data.append("Name: %s, Value: %s" %
                        (ps['by']['name'],
                         ps['value']))
        return '\n'.join(data)

    def take_action(self, parsed_args):
        rev = reviews.Query(parsed_args.host, parsed_args.port)

        to_filter = []
        if parsed_args.projects:
            pjs = parsed_args.projects
            projects = filters.OrFilter().add_items('project', pjs)
            to_filter.append(projects)

        other = filters.Items()
        other.add_items('is', ['open'])
        other.add_items('limit', parsed_args.limit)
        to_filter.append(other)

        columns = ('Subject', 'Project', 'Topic', 'Owner',
                   'Modified Time', 'Reviews', 'URL')

        data = []
        for review in rev.filter(*to_filter):
            last_updated = datetime.fromtimestamp(review['lastUpdated'])
            crvw = self._get_review_votes(review['currentPatchSet'])
            data.append((review['subject'][:50], review['project'],
                         review.get('topic'), review['owner']['name'],
                         last_updated, crvw, review['url']))

        return (columns, data)
