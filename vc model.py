import itertools
def shatterable_sets(points):
    shattered_sets = []
    for size in range(1, len(points) + 1):
        for subset in itertools.combinations(points, size):
            if is_shattered(subset, points):
                shattered_sets.append(subset)
    return shattered_sets

def is_shattered(subset, points):
    labels = {}
    for point in points:
        if point in subset:
            labels[point] = 1  
        else:
            labels[point] = 0

    for label_set in itertools.product([0, 1], repeat=len(subset)):
        labels_subset = {p: label_set[i] for i, p in enumerate(subset)}
        if set(labels_subset.values()) == {0, 1}:
            if labels_subset not in labels.values():
                return False
    return True

def vc_dimension(points):
    shattered_sets = shatterable_sets(points)
    vc_dim = max([len(ss) for ss in shattered_sets], default=0)
    return vc_dim

points = [(1, 1), (2, 2), (3, 3), (4, 4)]
dimension = vc_dimension(points)
print(f"VC dimension: {dimension}")



"""Vapnik-Chervonenkis Dimension
The Vapnik-Chervonenkis (VC) dimension is a measure of the capacity of a hypothesis set to
fit different data sets. It was introduced by Vladimir Vapnik and Alexey Chervonenkis in the 
1970s and has become a fundamental concept in statistical learning theory. The VC dimension 
is a measure of the complexity of a model, which can help us understand how well it can fit 
different data sets.

The VC dimension of a hypothesis set H is the largest number of points that can be shattered
by H. A hypothesis set H shatters a set of points S if, for every possible labeling of the points 
in S, there exists a hypothesis in H that correctly classifies the points. In other words, 
a hypothesis set shatters a set of points if it can fit any possible labeling of those points."""
