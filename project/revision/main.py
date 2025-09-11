from revision.functions_utils import is_number_bigger_than_given, add_salt_to_list


def main():
    result = is_number_bigger_than_given(candidate_number=5)
    print(result)

    result = is_number_bigger_than_given(candidate_number=66, threshold=1)
    print(result)

    add_salt_to_list([])


if __name__ == "__main__":
    main()
