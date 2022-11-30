import functions as f

manual = False

if manual:
    t = f.generateTotalArrayManual()
    print(f"T = {t}", end=f"\n\n")
    a = f.generateAllocatedMatrixManual()
    print(f"A = \n{a}", end=f"\n\n")
    m = f.generateMaxMatrixManual()
    print(f"M = \n{m}", end=f"\n\n")

else:
    t = f.generateTotalArrayAuto()
    print(f"T = {t}", end=f"\n\n")
    a = f.generateAllocatedMatrixAuto(t)
    print(f"A = \n{a}", end=f"\n\n")
    m = f.generateMaxMatrixAuto(t, a)
    print(f"M = \n{m}", end=f"\n\n")


v = f.calculateFirstAvailableResources(t, a)
print(f"V = {v}", end=f"\n\n")

wait = input("Press enter to show the solution...")

n = m - a
print(f"N = \n{n}", end=f"\n\n")

request = f.generateProcessToRequestResourcesAuto(n, t)
print(f"Request process: {request}")

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
    print("Proces trazi vise resursa!")
