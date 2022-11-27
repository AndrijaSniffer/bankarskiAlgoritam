import random
import numpy as np
import os
import constants as const

from numpy import ndarray

numberOfColumns = 0
numberOfRows = 0


def clear():
    os.system('cls')


def generateTotalArrayManual():
    global numberOfColumns
    clear()

    tn = int(input("Unesite velicinu \"Total\" niza: "))
    t = np.zeros(tn)

    for i in range(tn):
        t[i] = int(input("Unesite element total niza: "))

    numberOfColumns = tn
    return t


def generateTotalArrayAuto():
    global numberOfColumns
    clear()

    tn = random.randint(const.MIN_TOTAL_ARRAY, const.MAX_TOTAL_ARRAY)
    t = np.random.randint(const.MIN_TOTAL_ARRAY_VALUE, const.MAX_TOTAL_ARRAY_VALUE, tn, dtype=int)

    numberOfColumns = tn
    return t


def generateAllocatedMatrixManual():
    global numberOfRows
    clear()

    an = int(input("Unesite broj redova allocated i max matrice: "))
    numberOfRows = an

    a = np.zeros((numberOfRows, numberOfColumns), dtype=int)

    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            a[i][j] = int(input(f"Unesite element {j + 1}. {i + 1}-tog reda allocation matrice: "))

    return a


def generateAllocatedMatrixAuto(t):
    global numberOfRows
    clear()

    an = random.randint(const.MIN_AMN_ARRAY, const.MAX_AMN_ARRAY)
    numberOfRows = an

    a = np.random.randint(0, (np.max(t) - (random.randint(1, 3))), (an, numberOfColumns), dtype=int)

    while checkSumOfColumns(a, t):
        a = np.random.randint(0, (np.max(t) - (random.randint(1, 3))), (an, numberOfColumns), dtype=int)

    return a


def checkSumOfColumns(a, t):
    sumOfColumns = np.sum(a, axis=0)
    if (sumOfColumns >= t).any():
        return True
    return False


def generateMaxMatrixManual():
    clear()

    m = np.zeros((numberOfRows, numberOfColumns), dtype=int)

    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            m[i][j] = int(input(f"Unesite element {j + 1}. {i + 1}-tog reda max matrice: "))

    return m


def generateMaxMatrixAuto(t: ndarray, a: ndarray):
    m = np.zeros((numberOfRows, numberOfColumns), dtype=int)

    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            m[i][j] = random.randint(a[i][j], t[j])

    return m


def calculateFirstAvailableResources(t: ndarray, a: ndarray):
    aSums = np.sum(a, axis=0)

    return t - aSums


def generateProcessToRequestResourcesManual():
    prequestKey = int(input("Unesite koji proces ce zahtevati dodatne resurse(broj reda): ")) - 1
    prequestValue = np.zeros(numberOfColumns, dtype=int)

    for i in range(numberOfColumns):
        prequestValue[i] = int(input(f"Unesite koliko {i + 1}-tog resursa zeli da proces uzme: "))

    request = [prequestKey, prequestValue]
    return request


def generateProcessToRequestResourcesAuto(n: ndarray, t: ndarray):
    prequestKey = random.randint(0, numberOfRows - 1)
    prequestValue = np.zeros(numberOfColumns, dtype=int)

    for i in range(numberOfColumns - 1):
        maximum = min(n[prequestKey][i], np.min(t))
        if random.uniform(1, 6) == 5:
            prequestValue[i] = random.randint(0, maximum + 4)
        else:
            prequestValue[i] = random.randint(0, maximum)

    request = [prequestKey, prequestValue]
    return request


def checkConstraintsForRequesting(request, m: ndarray, v: ndarray):
    row = request[0]
    resources = request[1]
    firstCondition = False
    secondCondition = False

    if (m[row] >= resources).all():
        firstCondition = True
    if (v >= resources).all():
        secondCondition = True

    if firstCondition and secondCondition:
        return True
    return False


def attemptToMakeProcessSequence(a: ndarray, n: ndarray, v: ndarray):
    processNumber = -1
    iterations = -1
    processSequence = []
    processBlacklist = []

    while True:
        iterations = iterations + 1
        processNumber = processNumber + 1
        try:
            if len(processBlacklist) == numberOfRows:
                break

            if iterations == (numberOfRows * 10) and len(processBlacklist) != numberOfRows:
                break

            if processNumber == numberOfRows:
                processNumber = 0

            processBlacklist.index(processNumber)
            continue

        except ValueError:
            process = n[processNumber]

            if (process <= v).all():
                processSequence.append(f"P{processNumber}")
                processBlacklist.append(processNumber)
                v = v + a[processNumber]

    return processSequence
