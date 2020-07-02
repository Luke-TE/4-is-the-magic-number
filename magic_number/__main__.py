import sys
from num2words import num2words


def remove_punctuation(sentence):
    new_name = sentence.replace(' ', '')
    new_name = new_name.replace(',', '')
    new_name = new_name.replace('-', '')
    return new_name


def generate_sequence(curr):
    seq = [curr]
    while True:
        new = get_num_from_len(curr)
        if curr == new:
            break
        curr = new
        seq += [curr]

    return seq


def get_num_from_len(num):
    return len(remove_punctuation(num2words(num)))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Create a fun sequence.')
    parser.add_argument('num', metavar='n', type=int,
                        help='the number to start the sequence with.')

    args = parser.parse_args()

    seq = generate_sequence(args.num)
    seq_str = ",".join(map(str, seq))

    print("Sequence:", seq_str)
