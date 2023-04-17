import re
from typing import Union, TextIO, Iterator, Generator


def slice_limit(limit: int, it: Union[str, TextIO, Iterator, Generator]) -> Generator:
    i: int = 0
    for item in it:
        if i < limit:
            yield item
        else:
            break
        i += 1


def commands(cmd: str, value: str, data: Union[str, TextIO, Iterator, Generator]) -> Union[str, Iterator, Generator]:
    """
     :param cmd: the query command
     :param value: second subsidiary argument
     :param data: the name of file, that will be used
     :return: the list with the right answer
     """
    if cmd == 'filter':
        return filter(lambda x: value in x, data)
    elif cmd == 'map':
        return map(lambda x: x.split()[int(value)], data)
    elif cmd == 'unique':
        return iter(set(data))
    elif cmd == 'sort':
        return iter(sorted(data, reverse=value == 'desc'))
    elif cmd == 'limit':
        return slice_limit(int(value), data)
    elif cmd == 'regex':
        regex = re.compile(value)
        return filter(lambda r: regex.search(r), data)
    return ''
