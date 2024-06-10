from django.test import TestCase

# Create your tests here.
# Define score brackets and their corresponding sub-rank increments
# def faculty_ranks_list():
#     return [
#         ('Instructor I', 1),
#         ('Instructor II', 1),
#         ('Instructor III', 1),

#         ('Assistant Professor I', 1),
#         ('Assistant Professor II', 1),
#         ('Assistant Professor III', 1),
#         ('Assistant Professor IV', 1),

#         ('Associate Professor I', 1),
#         ('Associate Professor II', 1),
#         ('Associate Professor III', 1),
#         ('Associate Professor IV', 1),
#         ('Associate Professor V', 1),
        
#         ('Professor I', 1),
#         ('Professor II', 1),
#         ('Professor III', 1),
#         ('Professor IV', 1),
#         ('Professor V', 1),
#         ('Professor VI', 1),

#         ('University Professor', 1),
#     ]

# def get_rank_index(faculty_rank):
#     ranks = faculty_ranks_list()
#     for index, (rank, _) in enumerate(ranks):
#         if rank == faculty_rank:
#             return index
#     return None

# def points_bracket(points):
#     points_brackets = [
#         (41, 50, 1),
#         (51, 60, 2),
#         (61, 70, 3),
#         (71, 80, 4),
#         (81, 90, 5),
#         (91, 100, 6)
#     ]
#     for bracket in points_brackets:
#         if bracket[0] <= points <= bracket[1]:
#             return bracket[2]
#     # If points are less than 41, return 0
#     if points < 41:
#         return 0
#     return None

# def compute_total(points):
#     sub_rank_increment = points_bracket(points)
#     return sub_rank_increment

# def compute_new_rank(current_faculty_rank, points):
#     ranks = faculty_ranks_list()
#     rank_index = get_rank_index(current_faculty_rank)
#     if rank_index is not None:
#         result = compute_total(points)
#         if result is not None:
#             new_rank_index = rank_index + result
#             if new_rank_index >= len(ranks):
#                 new_rank_index = len(ranks) - 1
#             new_rank = ranks[new_rank_index][0]
#             return new_rank, result
#         else:
#             return current_faculty_rank, None
#     else:
#         return None, None

# # Example usage
# kra_one_score = 90.33
# final_points_for_kra_teaching = kra_one_score * 0.60
# current_faculty_rank = 'Instructor II'

# new_rank, result = compute_new_rank(current_faculty_rank, final_points_for_kra_teaching)
# if result is not None:
#     print(f"The points {final_points_for_kra_teaching:.2f} falls into a bracket with a sub-rank increment of {result}.")
#     print(f"Old Rank: {current_faculty_rank}, New Rank: {new_rank}")
# else:
#     print("Points do not fall into any bracket or invalid faculty rank.")



# def faculty_ranks_list():
#     return [
#         ('Instructor I', 1),
#         ('Instructor II', 1),
#         ('Instructor III', 1),
#         ('Assistant Professor I', 1),
#         ('Assistant Professor II', 1),
#         ('Assistant Professor III', 1),
#         ('Assistant Professor IV', 1),
#         ('Associate Professor I', 1),
#         ('Associate Professor II', 1),
#         ('Associate Professor III', 1),
#         ('Associate Professor IV', 1),
#         ('Associate Professor V', 1),
#         ('Professor I', 1),
#         ('Professor II', 1),
#         ('Professor III', 1),
#         ('Professor IV', 1),
#         ('Professor V', 1),
#         ('Professor VI', 1),
#         ('University Professor', 1),
#     ]


# def get_rank_index(faculty_rank):
#     ranks = faculty_ranks_list()
#     for index, (rank, _) in enumerate(ranks):
#         if rank == faculty_rank:
#             return index
#     return None


# def points_bracket(points):
#     points_brackets = [
#         (41, 50, 1),
#         (51, 60, 2),
#         (61, 70, 3),
#         (71, 80, 4),
#         (81, 90, 5),
#         (91, 100, 6)
#     ]
#     for bracket in points_brackets:
#         if bracket[0] <= points <= bracket[1]:
#             return bracket[2]
#     # If points are less than 41, return 0
#     if points < 41:
#         return 0
#     return None


# def compute_total(points):
#     sub_rank_increment = points_bracket(points)
#     return sub_rank_increment


# def kra_one_teachingeffectiveness(faculty_rank):
#     if 'Instructor' in faculty_rank:
#         return 0.60
#     elif 'Assistant Professor' in faculty_rank:
#         return 0.50
#     elif 'Associate Professor' in faculty_rank:
#         return 0.40
#     elif 'Professor' in faculty_rank:
#         return 0.30
#     elif 'University Professor' in faculty_rank:
#         return 0.20
#     else:
#         return 0  # Default value

# def kra_two_researchpublications(faculty_rank):
#     pass

# def kra_three_professionaldevelopment(faculty_rank):
#     pass

# def kra_four_extensionservices(faculty_rank):
#     pass


# def compute_new_rank(current_faculty_rank, kra_one_score):
#     percentage = kra_one_teachingeffectiveness(current_faculty_rank)
#     final_points_for_kra_teaching = kra_one_score * percentage
#     final_points_for_kra_research = kra_two_score * percentage
#     final_points_for_kra_prodevlp = kra_three_score * percentage
#     final_points_for_kra_extservc = kra_four_score * percentage
#     ranks = faculty_ranks_list()
#     rank_index = get_rank_index(current_faculty_rank)
    
#     if rank_index is not None:
#         result1 = compute_total(final_points_for_kra_teaching)
#         result2 = compute_total(final_points_for_kra_research)
#         result3 = compute_total(final_points_for_kra_prodevlp)
#         result4 = compute_total(final_points_for_kra_extservc)


#         if result is not None:
#             new_rank_index = rank_index + result
#             if new_rank_index >= len(ranks):
#                 new_rank_index = len(ranks) - 1
#             new_rank = ranks[new_rank_index][0]
#             return new_rank, final_points_for_kra_teaching, result
#         else:
#             return current_faculty_rank, final_points_for_kra_teaching, None
#     else:
#         return None, None, None

# def add_all_kra(request):
#     # add the follownig and get the final result
#         # result1 = compute_total(final_points_for_kra_teaching)
#         # result2 = compute_total(final_points_for_kra_research)
#         # result3 = compute_total(final_points_for_kra_prodevlp)
#         # result4 = compute_total(final_points_for_kra_extservc)
#     # the final pts result will then refer to points bracket and then will evaluate the new rank

# # Example usage
# kra_one_score = 90.43
# kra_two_score = 100
# kra_three_score = 12.65
# kra_four_score = 7.50
# current_faculty_rank = 'Instructor III'

# new_rank, final_points_for_kra_teaching, final_points_for_kra_research, final_points_for_kra_prodevlp, final_points_for_kra_extservc, result = compute_new_rank(current_faculty_rank, kra_one_score)
# if result is not None:
#     print(f"The points for KRA 1 {final_points_for_kra_teaching:.2f}.")
#     print(f"The points for KRA 2 {final_points_for_kra_research:.2f}.")
#     print(f"The points for KRA 3 {final_points_for_kra_prodevlp:.2f}.")
#     print(f"The points for KRA 4 {final_points_for_kra_extservc:.2f}.")
#     print (f'final result falls into a bracket with a sub-rank increment of {result}')
#     print(f"Old Rank: {current_faculty_rank}, New Rank: {new_rank}")
# else:
#     print("Points do not fall into any bracket or invalid faculty rank.")




def faculty_ranks_list():
    return [
        ('Instructor I', 1),
        ('Instructor II', 1),
        ('Instructor III', 1),
        ('Assistant Professor I', 1),
        ('Assistant Professor II', 1),
        ('Assistant Professor III', 1),
        ('Assistant Professor IV', 1),
        ('Associate Professor I', 1),
        ('Associate Professor II', 1),
        ('Associate Professor III', 1),
        ('Associate Professor IV', 1),
        ('Associate Professor V', 1),
        ('Professor I', 1),
        ('Professor II', 1),
        ('Professor III', 1),
        ('Professor IV', 1),
        ('Professor V', 1),
        ('Professor VI', 1),
        ('University Professor', 1),
    ]

def get_rank_index(faculty_rank):
    ranks = faculty_ranks_list()
    for index, (rank, _) in enumerate(ranks):
        if rank == faculty_rank:
            return index
    return None

def points_bracket(points):
    points_brackets = [
        (41, 50, 1),
        (51, 60, 2),
        (61, 70, 3),
        (71, 80, 4),
        (81, 90, 5),
        (91, 100, 6)
    ]
    for bracket in points_brackets:
        if bracket[0] <= points <= bracket[1]:
            return bracket[2]
    # If points are less than 41, return 0
    if points < 41:
        return 0
    return None

def compute_total(points):
    sub_rank_increment = points_bracket(points)
    return sub_rank_increment

def kra_one_teachingeffectiveness(faculty_rank):
    if 'Instructor' in faculty_rank:
        return 0.60
    elif 'Assistant Professor' in faculty_rank:
        return 0.50
    elif 'Associate Professor' in faculty_rank:
        return 0.40
    elif 'Professor' in faculty_rank:
        return 0.30
    elif 'University Professor' in faculty_rank:
        return 0.20
    else:
        return 0  # Default value

def kra_two_researchpublications(faculty_rank):
    if 'Instructor' in faculty_rank:
        return 0.10
    elif 'Assistant Professor' in faculty_rank:
        return 0.20
    elif 'Associate Professor' in faculty_rank:
        return 0.30
    elif 'Professor' in faculty_rank:
        return 0.40
    elif 'University Professor' in faculty_rank:
        return 0.50
    else:
        return 0  # Default value

def kra_three_professionaldevelopment(faculty_rank):
    return 0.20  # Fixed percentage for all ranks

def kra_four_extensionservices(faculty_rank):
    return 0.10  # Fixed percentage for all ranks

def compute_new_rank(current_faculty_rank_func, kra_one_score, kra_two_score, kra_three_score, kra_four_score):
    # If the input is a function, call it to get the current rank
    if callable(current_faculty_rank_func):
        current_faculty_rank = current_faculty_rank_func()
    else:
        current_faculty_rank = current_faculty_rank_func

    # Rest of the function remains the same
    percentage1 = kra_one_teachingeffectiveness(current_faculty_rank)
    percentage2 = kra_two_researchpublications(current_faculty_rank)
    percentage3 = kra_three_professionaldevelopment(current_faculty_rank)
    percentage4 = kra_four_extensionservices(current_faculty_rank)

    final_points_for_kra_teaching = kra_one_score * percentage1
    final_points_for_kra_research = kra_two_score * percentage2
    final_points_for_kra_prodevlp = kra_three_score * percentage3
    final_points_for_kra_extservc = kra_four_score * percentage4

    total_points = (final_points_for_kra_teaching + 
                    final_points_for_kra_research + 
                    final_points_for_kra_prodevlp + 
                    final_points_for_kra_extservc)

    ranks = faculty_ranks_list()
    rank_index = get_rank_index(current_faculty_rank)
    
    if rank_index is not None:
        result = compute_total(total_points)
        if result is not None:
            new_rank_index = rank_index + result
            if new_rank_index >= len(ranks):
                new_rank_index = len(ranks) - 1
            new_rank = ranks[new_rank_index][0]

            # Determine impression
            impression = 'promoted' if result > 0 else 'retain'

            return new_rank, total_points, result, impression
        else:
            return current_faculty_rank, total_points, None, None
    else:
        return None, None, None, None

# Example usage
def thefaculty():
    return 'Associate Professor V'

kra_one_score = 100
kra_two_score = 87.5
kra_three_score = 63.25
kra_four_score = 75

new_rank, total_points, result, impression = compute_new_rank(thefaculty, kra_one_score, kra_two_score, kra_three_score, kra_four_score)
if result is not None:
    print(f"The total points {total_points:.2f} fall into a bracket with a sub-rank increment of {result}.")
    print(f"Old Rank: {thefaculty()}, New Rank: {new_rank}, Impression: {impression}")
else:
    print("Points do not fall into any bracket or invalid faculty rank.")

