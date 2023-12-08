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
    

def processNextStage(seeds: list[range], transform: list[tuple]) -> list[range]:
    print(f"processing map: {transform}")
    transformedSeeds = []
    for seedRange in seeds:
        print(f"new seed range! {seedRange}")
        firstVal = seedRange.start
        lastVal = seedRange.stop
        for dst, src, rg in transform:
            if firstVal < src and src + rg <= lastVal: # our transformation is fully within this range
                print(f"Our map is in bounds! Transfering ({src}, {src + rg}) -> ({dst}, {dst + rg})")
                transformedSeeds.append(range(dst, dst + rg))
                if lastVal - (src + rg) > 1: 
                    print(f"also adding ({src + rg}, {lastVal})")
                    transformedSeeds.append(range(src + rg, lastVal)) # add the remaining upper and lower bounds
                if src - firstVal > 1: 
                    print(f"also adding ({firstVal}, {src})")
                    transformedSeeds.append(range(firstVal, src))
                break
            if firstVal < src: # lower bound of map is within range, upper bound is not (src + rg > lastVal), new range is to (lastVal - firstVal)
                print(f"Upper range {lastVal} out of bounds for {src + rg}, Transfering ({src}, {src + (lastVal - firstVal)}) to ({dst}, {dst + (lastVal - firstVal)})")
                transformedSeeds.append(range(dst, dst + (lastVal - firstVal)))
                if src - firstVal > 1: 
                    print(f"also adding ({firstVal}, {src})")
                    transformedSeeds.append(range(firstVal, src))
                break
            if src + rg <= lastVal: # upper bound of map is within range, lower bound is not (firstVal >= src), 
                print(f"Lower range {firstVal} out of bounds for {src}, Transfering ({src + (firstVal - src)}, {src + dst}) to ({dst + (firstVal - src)}, {dst + rg})")
                transformedSeeds.append(range(dst + (firstVal - src), dst + rg))
                if lastVal - (src + rg) > 1: 
                    print(f"also adding ({src + rg}, {lastVal})")
                    transformedSeeds.append(range(src + rg, lastVal)) 
                break
    return transformedSeeds

            






def minSeedJourney2ElectricBoogaloo(path: str) -> int:
    with open(path, "r") as f:
        seedPairs = map(lambda x: int(x), f.readline()[7:].split()) # remove "seeds: ", convert all the numbers to ints
        seedsToPlant = list(map(lambda x: range(x[0], x[0]+x[1]), itertools.batched(seedPairs, 2)))
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print("initial")
        print(seedsToPlant)
        
        transformMap = []
        # seed-to-soil map
        while (ln := f.readline()) != "\n":
            transformMap.append(tuple(map(lambda x: int(x), ln.split())))

        seedsToPlant = processNextStage(seedsToPlant, transformMap)

        raise Exception("fuck you lol")
        

        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print("seed to soil")
        print(seedsToPlant)

        transformMap = []
        # soil-to-fertilizer map
        while (ln := f.readline()) != "\n":
            transformMap.append(tuple(map(lambda x: int(x), ln.split())))

        seedsToPlant = processNextStage(seedsToPlant, transformMap)
        

        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print("soil to fert")
        print(seedsToPlant)

        transformMap = []
        # fertilizer-to-water map
        while (ln := f.readline()) != "\n":
            transformMap.append(tuple(map(lambda x: int(x), ln.split())))

        seedsToPlant = processNextStage(seedsToPlant, transformMap)

        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print("fert to water")
        print(seedsToPlant)

        transformMap = []
        # water-to-light map
        while (ln := f.readline()) != "\n":
            transformMap.append(tuple(map(lambda x: int(x), ln.split())))

        seedsToPlant = processNextStage(seedsToPlant, transformMap)

        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print("water to light")
        print(seedsToPlant)

        transformMap = []
        # light-to-temperature map
        while (ln := f.readline()) != "\n":
            transformMap.append(tuple(map(lambda x: int(x), ln.split())))

        seedsToPlant = processNextStage(seedsToPlant, transformMap)

        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print("light to temp")
        print(seedsToPlant)

        transformMap = []
        # temperature-to-humidity map
        while (ln := f.readline()) != "\n":
            transformMap.append(tuple(map(lambda x: int(x), ln.split())))

        seedsToPlant = processNextStage(seedsToPlant, transformMap)

        
        while (ln := f.readline()) == "\n": # read away newlines and map headers
            continue

        print("temp to humid")
        print(seedsToPlant)

        transformMap = []
        # humidity-to-location map
        while (ln := f.readline()) != "\n":
            if ln == "": break
            transformMap.append(tuple(map(lambda x: int(x), ln.split())))

        seedsToPlant = processNextStage(seedsToPlant, transformMap)

        print("FINAL locations")
        print(seedsToPlant)

        return min(list(map(lambda x: x.start, seedsToPlant)))



if __name__ == "__main__":
    part1Ans = minSeedJourneyExtravaganza("./input.txt")
    print(f"Part 1 answer: {part1Ans}")

    part2Ans = minSeedJourney2ElectricBoogaloo("./sample.txt")
    print(f"Part 2 answer: {part2Ans}")
        
