import itertools


def minSeedJourneyExtravaganza(path: str) -> int:
    with open(path, "r") as f:
        seedsToPlant = list(map(lambda x: int(x), f.readline()[7:].split())) # remove "seeds: ", convert all the numbers to ints
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue
        
        # seed-to-soil map
        doNotChange = []
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            for i in range(len(seedsToPlant)):
                if i in doNotChange: continue
                try:
                    seedsToPlant[i] = range(src, src+rg).index(seedsToPlant[i]) + dst
                    doNotChange.append(i)
                except ValueError:
                    pass # leave this element the same if its not in range
                except:
                    print("some other error!!!!")
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        # soil-to-fertilizer map
        doNotChange = []
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            for i in range(len(seedsToPlant)):
                if i in doNotChange: continue
                try:
                    seedsToPlant[i] = range(src, src+rg).index(seedsToPlant[i]) + dst
                    doNotChange.append(i)
                except ValueError:
                    pass # leave this element the same if its not in range
                except:
                    print("some other error!!!!")
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        # fertilizer-to-water map
        doNotChange = []
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            for i in range(len(seedsToPlant)):
                if i in doNotChange: continue
                try:
                    seedsToPlant[i] = range(src, src+rg).index(seedsToPlant[i]) + dst
                    doNotChange.append(i)
                except ValueError:
                    pass # leave this element the same if its not in range
                except:
                    print("some other error!!!!")
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        # water-to-light map
        doNotChange = []
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            for i in range(len(seedsToPlant)):
                if i in doNotChange: continue
                try:
                    seedsToPlant[i] = range(src, src+rg).index(seedsToPlant[i]) + dst
                    doNotChange.append(i)
                except ValueError:
                    pass # leave this element the same if its not in range
                except:
                    print("some other error!!!!")
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        # light-to-temperature map
        doNotChange = []
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            for i in range(len(seedsToPlant)):
                if i in doNotChange: continue
                try:
                    seedsToPlant[i] = range(src, src+rg).index(seedsToPlant[i]) + dst
                    doNotChange.append(i)
                except ValueError:
                    pass # leave this element the same if its not in range
                except:
                    print("some other error!!!!")
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        # temperature-to-humidity map
        doNotChange = []
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            for i in range(len(seedsToPlant)):
                if i in doNotChange: continue
                try:
                    seedsToPlant[i] = range(src, src+rg).index(seedsToPlant[i]) + dst
                    doNotChange.append(i)
                except ValueError:
                    pass # leave this element the same if its not in range
                except:
                    print("some other error!!!!")
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        # humidity-to-location map
        doNotChange = []
        while (ln := f.readline()) != "\n":
            if ln == "": break
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            for i in range(len(seedsToPlant)):
                if i in doNotChange: continue
                try:
                    seedsToPlant[i] = range(src, src+rg).index(seedsToPlant[i]) + dst
                    doNotChange.append(i)
                except ValueError:
                    pass # leave this element the same if its not in range
                except:
                    print("some other error!!!!")
        
        return min(seedsToPlant)
    



def minSeedJourney2ElectricBoogaloo(path: str) -> int:
    with open(path, "r") as f:
        seedPairs = list(map(lambda x: int(x), f.readline()[7:].split())) # remove "seeds: ", convert all the numbers to ints
        seedsToPlant = itertools.chain.from_iterable(map(lambda x: list(range(x[0], x[0]+x[1])), sorted(itertools.batched(seedPairs, 2), key=lambda y: y[0])))
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue
        
        # seed-to-soil map
        seedSoil = {} # tuple -> range
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            seedSoil[(dst, src, rg)] = range(src, src+rg)
            newRange = range(src, src+rg)
        # for i in range(len(seedsToPlant)):
        #     for (key, val) in seedSoil.items():
        #         if (item := seedsToPlant[i]) in val:
        #             dst, src, rg = key
        #             seedsToPlant[i] = item - (src - dst)
        #             break
        
        for ((dst, src, rg), rangeObj) in seedSoil.items():
            firstVal = rangeObj.start
            secondVal = rangeObj.stop - 1
            ind = seedsToPlant.index(firstVal)
            for i in range(rg):
                if seedsToPlant[i] > secondVal:
                    break

        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print(seedsToPlant)

        # soil-to-fertilizer map
        soilFert = {}
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            seedSoil[(dst, src, rg)] = range(src, src+rg)
        for i in range(len(seedsToPlant)):
            for (key, val) in soilFert.items():
                if (item := seedsToPlant[i]) in val:
                    dst, src, rg = key
                    seedsToPlant[i] = item - (src - dst)
                    break
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print(seedsToPlant)

        # fertilizer-to-water map
        fertWater = {}
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            fertWater[(dst, src, rg)] = range(src, src+rg)
        for i in range(len(seedsToPlant)):
            for (key, val) in fertWater.items():
                if (item := seedsToPlant[i]) in val:
                    dst, src, rg = key
                    seedsToPlant[i] = item - (src - dst)
                    break
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print(seedsToPlant)

        # water-to-light map
        waterLight = {}
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            waterLight[(dst, src, rg)] = range(src, src+rg)
        for i in range(len(seedsToPlant)):
            for (key, val) in waterLight.items():
                if (item := seedsToPlant[i]) in val:
                    dst, src, rg = key
                    seedsToPlant[i] = item - (src - dst)
                    break
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print(seedsToPlant)

        # light-to-temperature map
        lightTemp = {}
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            lightTemp[(dst, src, rg)] = range(src, src+rg)
        for i in range(len(seedsToPlant)):
            for (key, val) in lightTemp.items():
                if (item := seedsToPlant[i]) in val:
                    dst, src, rg = key
                    seedsToPlant[i] = item - (src - dst)
                    break
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print(seedsToPlant)

        # temperature-to-humidity map
        tempHumid = {}
        while (ln := f.readline()) != "\n":
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            tempHumid[(dst, src, rg)] = range(src, src+rg)
        for i in range(len(seedsToPlant)):
            for (key, val) in tempHumid.items():
                if (item := seedsToPlant[i]) in val:
                    dst, src, rg = key
                    seedsToPlant[i] = item - (src - dst)
                    break
        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print(seedsToPlant)

        # humidity-to-location map
        humidLoc = {}
        while (ln := f.readline()) != "\n":
            if ln == "": break
            dst, src, rg = tuple(map(lambda x: int(x), ln.split()))
            lightTemp[(dst, src, rg)] = range(src, src+rg)
        for i in range(len(seedsToPlant)):
            for (key, val) in humidLoc.items():
                if (item := seedsToPlant[i]) in val:
                    dst, src, rg = key
                    seedsToPlant[i] = item - (src - dst)
                    break

        print(seedsToPlant)

        return min(seedsToPlant)



if __name__ == "__main__":
    part1Ans = minSeedJourneyExtravaganza("./input.txt")
    print(f"Part 1 answer: {part1Ans}")

    part2Ans = minSeedJourney2ElectricBoogaloo("./sample.txt")
    print(f"Part 2 answer: {part2Ans}")
        
