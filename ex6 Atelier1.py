def tri_a_bulle(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def tri_par_selection(nums):
    for i in range(len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

def tri_par_insertion(nums):

    for i in range(1, len(nums)):
        element_a_inserer = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > element_a_inserer:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = element_a_inserer

