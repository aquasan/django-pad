
# /utils/paginator.py - Beylog
#
# Copyright (c) 2006 beyking@gmail.com
# Distributed under the GPL License (See http://www.gnu.org/copyleft/gpl.html)
#


class Paginator(object):

    def __init__(self, obj_list, num_per_page):
        self.obj_list = obj_list
        self.num_per_page = num_per_page

    def getPage(self, page_index):
        page_list = []
        cur_index = 1
        max_index = 1

        if self.obj_list:
            max_index, over = divmod(len(self.obj_list), self.num_per_page)
            if over != 0: max_index += 1
            if max_index < 1: max_index = 1

            cur_index = int(page_index)
            if cur_index < 1: cur_index = 1
            if cur_index > max_index: cur_index = max_index

            offset = (cur_index - 1) * self.num_per_page
            page_list = list(self.obj_list[offset: offset + self.num_per_page])

        return cur_index, max_index, page_list
