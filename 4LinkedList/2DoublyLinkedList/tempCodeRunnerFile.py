
        new_node.next = store
        if store:
            store.prev = new_node
    return head_node