import re

from rest_framework import pagination
from rest_framework.response import Response

max_format_validity_check = re.compile(r'^\+880[1-9]{10}$')
min_format_validity_check = re.compile(r'^0[1-9]{10}$')
number_regex = re.compile(r'0[1-9]{10}$')
third_valid_digits = [3, 7, 6, 8, 4, 9, 5]

valid_number_length = [11, 14]


def valid_blood_groups():
    return ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 30

    def get_paginated_response(self, data):
        return Response(
            {
                'status': 'success',
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link(),
                },
                'count': self.page.paginator.count,
                'total_pages': self.page.paginator.num_pages,
                'results': data,
            }
        )


def normalize_mobile_number(mobile_number):
    if len(mobile_number) in valid_number_length:
        number = None
        if len(mobile_number) == 14:
            if max_format_validity_check.search(mobile_number):
                number = number_regex.search(mobile_number).group()
        else:
            if min_format_validity_check.search(mobile_number):
                number = number_regex.search(mobile_number).group()

        if number:
            if int(number[2]) not in third_valid_digits:
                number = None

        return number
