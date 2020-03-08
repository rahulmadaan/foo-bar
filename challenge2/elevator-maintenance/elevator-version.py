def manage_previous_group(ele1, ele2, index):
    if index <= 0:
        return True
    else:
        return int(ele1[index - 1]) >= int(ele2[index - 1]) and manage_previous_group(ele1, ele2, index - 1)


def manage_current_group(ele1, ele2, group):
    return int(ele1[group]) > int(ele2[group])


def sort(arr, group=0):
    for times in range(0, len(arr)):
        for index in range(0, len(arr) - 1):
            first_no, second_no = arr[index], arr[index + 1]
            previous_group = manage_previous_group(first_no, second_no, group)
            current_group = manage_current_group(first_no, second_no, group)
            if previous_group and current_group:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    return arr


def sort_versions(arr):
    one = sort(arr, 0)
    two = sort(one, 1)
    return sort(two, 2)


def split_with_dot(ele):
    return ele.split(".")


def format_output(output):
    return map(".".join, output)
    # return ",".join(map(".".join, output))


def fill_elements(arr, times):
    for time in range(0, times):
        arr.append("-1")
    return arr


def validate(input):
    shortage = len(input) % 3
    if 3 > shortage > 0:
        return fill_elements(input, 3 - shortage)
    else:
        return input


def remove_unnecessary(ele):
    if ele.count("-1") > 0:
        ele.pop()
        return remove_unnecessary(ele)
    else:
        return ele


def sanitize_output(output):
    return map(remove_unnecessary, output)


def sanitize_input(input):
    versions = map(split_with_dot, input)
    return map(validate, versions)


def solution(version_list):
    sanitized_input = sanitize_input(version_list)
    sorted_versions = sort_versions(sanitized_input)
    sanitized_output = sanitize_output(sorted_versions)
    result = format_output(sanitized_output)
    return result
