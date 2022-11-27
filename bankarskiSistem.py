import random
import numpy as np

import functions as f

manual = False

if manual:
    t = f.generateTotalArrayManual()
    a = f.generateAllocatedMatrixManual()
    m = f.generateMaxMatrixManual()

else:
    t = f.generateTotalArrayAuto()
    print(t, end=f"\n\n")
    a = f.generateAllocatedMatrixAuto(t)
    print(a, end=f"\n\n")
    m = f.generateMaxMatrixAuto(t, a)
    print(m, end=f"\n\n")


v = f.calculateFirstAvailableResources(t, a)
print(v, end=f"\n\n")
n = m - a
print(n, end=f"\n\n")


request = f.generateProcessToRequestResourcesAuto(n, t)
print(request)

if f.checkConstraintsForRequesting(request, m, v):
    row = request[0]
    requestedResousces = request[1]
    v = v - requestedResousces

    a[row] = a[row] + requestedResousces

    processSequence = f.attemptToMakeProcessSequence(a, n, v)

    if len(processSequence) == f.numberOfRows:
        print(f"Sekvenca je sigurna: {processSequence}")
    else:
        print(f"Sekvenca je nesigurna: {processSequence}")

else:
    print("Proces trazi vise resursa nego sto je najavio da ce koristiti")
