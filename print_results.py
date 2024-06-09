#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results
#          dictionary (results_dic).
#         This function inputs:
#            -The results dictionary as results_dic within print_results
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main.
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function.
#       Notice that this function doesn't to return anything because it
#       prints a summary of the results using results_dic and results_stats_dic
#

def print_incorrect_dog_images(results_dic):
    print("\n Incorrect Dog/NOT Dog Assignments: ")

    for key, values in results_dic.items():
        label, classified, match, is_dog, classified_as_dog = values

        if (match == 0) and (is_dog == 0 or classified_as_dog == 0):
            print("Real: {:20}    Classifier: {:20}".format(label, classified))


def print_incorrect_breeds(results_dic):
    print("\n Incorrect Dog Breed Assignments: ")

    for key, values in results_dic.items():
        label, classified, match, is_dog, classified_as_dog = values

        if (match == 0) and (is_dog == 1 and classified_as_dog == 1):
            print("Real: {:20}    Classifier: {:20}".format(label, classified))


def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(),
          "***")

    print("{:20}: {:3d}".format('N Images: ', results_stats_dic['n_images']))

    print("{:20}: {:3d}".format('N Dog Images: ', results_stats_dic['n_dogs_img']))

    print("{:20}: {:3d}".format('N Not Dog Images: ', results_stats_dic['n_notdogs_img']))

    print("{:20}: {:.2f}%".format('PCT Match: ', results_stats_dic['pct_match']))

    print("{:20}: {:.2f}%".format('PCT Correct Dogs: ', results_stats_dic['pct_correct_dogs']))

    print("{:20}: {:.2f}%".format('PCT Correct Breed: ', results_stats_dic['pct_correct_breed']))

    print("{:20}: {:.2f}%".format('PCT Correct Not Dogs: ', results_stats_dic['pct_correct_notdogs']))

    print_incorrect_dog_images(results_dic)

    print_incorrect_breeds(results_dic)
