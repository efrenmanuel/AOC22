trees = []
visible = 0


def p1():
    with open("input1.txt", "r") as inputFile:
        lines = inputFile.read().split()
        trees = [list(line) for line in lines]
        # borders minus duped corners
        visible = len(trees)*2 + len(trees[0])*2 - 4
        for row in trees:
            print(row)
        for row in zip(*trees):
            print(row)
        inner_width=len(trees[0])-2
        for tree_num in range(0, (len(trees)-2)*inner_width):
            tree_col_index = tree_num % inner_width + 1
            tree_row_index = tree_num // inner_width + 1
            trees_rotated = list(zip(*trees))
            tree = trees[tree_row_index][tree_col_index]
            tree_visible = False

            if (max(trees[tree_row_index][:tree_col_index]) < tree or
                    max(trees[tree_row_index][tree_col_index+1:]) < tree):
                tree_visible = True
            elif (max(trees_rotated[tree_col_index][:tree_row_index]) < tree or
                    max(trees_rotated[tree_col_index][tree_row_index+1:]) < tree):
                tree_visible = True
            visible += tree_visible

        print(visible)

def calculate_view_distance(tree, array):
    view_distance=0
    for other_tree in array:
        view_distance+=1
        if other_tree >= tree:
            break
    
    return view_distance

def p2():
    with open("input1.txt", "r") as inputFile:
        lines = inputFile.read().split()
        trees = [list(line) for line in lines]
        visible_arr = []
        for tree_num in range(0, len(trees)*len(trees[0])):
            score=1
            tree_col_index = tree_num % len(trees[0])
            tree_row_index = tree_num // len(trees[0])
            trees_rotated = list(zip(*trees))
            tree = trees[tree_row_index][tree_col_index]

            if (tree_col_index < len(trees[0])-1):
                score*=calculate_view_distance(tree, trees[tree_row_index][tree_col_index+1:])
                '''view_distance=0
                for other_tree in trees[tree_row_index][tree_col_index+1:]:
                    view_distance+=1
                    if other_tree >= tree:
                        score*=view_distance
                        break'''
            
            if (tree_col_index > 0):
                score*=calculate_view_distance(tree, trees[tree_row_index][tree_col_index-1::-1])
                '''view_distance=0
                for other_tree in trees[tree_row_index][tree_col_index-1::-1]:
                    visible+=1
                    if other_tree >= tree:
                        break'''
            
            if (tree_row_index > 0):
                score*=calculate_view_distance(tree, trees_rotated[tree_col_index][tree_row_index-1::-1])
                '''view_distance=0
                for other_tree in trees_rotated[tree_col_index][tree_row_index-1::-1]:
                    visible+=1
                    if other_tree >= tree:
                        break'''

            if (tree_row_index < len(trees)-1):
                score*=calculate_view_distance(tree, trees_rotated[tree_col_index][tree_row_index+1:])
                '''view_distance=0
                for other_tree in trees_rotated[tree_col_index][tree_row_index+1:]:
                    visible+=1
                    if other_tree >= tree:
                        break'''

            visible_arr.append(score)

        print(max(visible_arr))


p2()
