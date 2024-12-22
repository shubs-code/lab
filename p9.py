from collections import deque

def fifo_page_replacement(pages, frame_count):
    memory = deque(maxlen=frame_count)
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frame_count:
                memory.append(page)
            else:
                memory.popleft()
                memory.append(page)
            page_faults += 1
    return page_faults

def lru_page_replacement(pages, frame_count):
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frame_count:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
        else:
            memory.remove(page)
            memory.append(page)
    return page_faults

def optimal_page_replacement(pages, frame_count):
    memory = []
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]
        if page not in memory:
            if len(memory) < frame_count:
                memory.append(page)
            else:
                farthest_use = -1
                page_to_replace = -1
                for mem_page in memory:
                    try:
                        next_use = pages.index(mem_page, i+1)
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest_use:
                        farthest_use = next_use
                        page_to_replace = mem_page
                memory.remove(page_to_replace)
                memory.append(page)
            page_faults += 1
    return page_faults


pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
frame_count = 3
print(f"FIFO Page Faults: {fifo_page_replacement(pages, frame_count)}")
print(f"LRU Page Faults: {lru_page_replacement(pages, frame_count)}")
print(f"Optimal Page Faults: {optimal_page_replacement(pages, frame_count)}")
