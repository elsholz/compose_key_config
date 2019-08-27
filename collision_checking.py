"""This module checks if any key combinations are ambiguous."""


class UnionTrie:
    """A trie with one speciality: A Node can either contain a value or have a dictionary of sub nodes.
    The goal of this data structure it to provide a way to recognize conflicts when inserting new character
    combinations.

    Example:
        Given the following AtomicTrie

               -----O-----
              |r    |f    |s
              …     O     …
                    |a
                    O
                   <∀>

        If we want to use the key combination <fax> to produce <☎>️, then there would be an obvious conflict.
        The AtomicTrie would not allow our node that already has the value <∀> to receive a seconds mapping,
        or get overwritten.
    """

    def __init__(self, value=None):
        """Create empty node with an empty list of sub nodes."""
        self.sub_nodes = None
        self.value = None

        if value:
            self.value = value
        else:
            self.sub_nodes = {}

    def insert(self, value, route):
        ve = ValueError('Value can\'t be inserted!')
        if self.value is not None:
            raise ve

        if len(route) == 1:
            if not route[0] in self.sub_nodes:
                self.sub_nodes[route[0]] = UnionTrie(value=value)
            else:
                raise ve
        else:
            sub_trie = self.sub_nodes.get(route[0], UnionTrie())
            self.sub_nodes[route[0]] = sub_trie
            sub_trie.insert(value, route[1:])

    def __str__(self):
        if self.sub_nodes:
            # return [f'{k}: {str(v)}' for k, v in self.sub_nodes.items()]
            return 'UnionTree(sub_nodes=' + ', '.join([str({'"'+k+'"': str(v)}) for k, v in self.sub_nodes.items()]).replace(
                '\'', "") + ')'
        elif self.value:
            return 'UnionTree(value=' + str(self.value) + ')'
        else:
            return 'UnionTrie()'
