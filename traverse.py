def traverse(root, prefix):
    ''' обход дерева '''
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    ans = traverse(root['left'], prefix)
    prefix.pop()
    prefix.append('1')
    ans.extend(traverse(root['right'], prefix))
    prefix.pop()
    return ans
