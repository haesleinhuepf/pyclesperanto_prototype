import pyclesperanto_prototype as cle
import numpy as np

def test_maximum_sphere():
    test = cle.push(np.asarray([
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ]))

    test2 = cle.create(test)
    cle.maximum_sphere(test, test2, 1, 1, 1)

    a = cle.pull(test2)
    assert (np.min(a) == 1)
    assert (np.max(a) == 2)

    cle.set(test, 5)
    # print(test)
    # print(cle.pull(test))

    a = cle.pull(test)
    assert (np.min(a) == 5)
    assert (np.max(a) == 5)
    assert (np.mean(a) == 5)

    print("ok maximum sphere")
