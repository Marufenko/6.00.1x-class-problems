'''
https://courses.edx.org/courses/course-v1:MITx+6.00.1x_9+2T2016/courseware/Week_10/Problem_Set_6/
'''

import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = (location[0] * 1.0, location[1] * 1.0)

    def get_name(self):
        # return the name of the adoption center
        return self.name

    def get_location(self):
        # return location of adoption center
        self.float_location = (float(self.location[0]), float(self.location[1]))
        return self.float_location

    def get_species_count(self):
        # return dict of available pets in adoption center
        copy_species_count = {}
        for name in self.species_types:
            if self.species_types[name] > 0:
                copy_species_count[name] = self.species_types[name]
        return copy_species_count
        
    def get_number_of_species(self, animal):
        # return number of apecified animal in adoption center
        if animal not in self.get_species_count():
            number = 0
        else:
            number = self.get_species_count()[animal]
        return number

    def adopt_pet(self, species):
        # update the value for specified pet on "-1" value
        if species in self.get_species_count():
            if self.get_species_count()[species] == 1:
                del self.species_count[species_name]
            else:
                self.species_types[species] -= 1



class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        # return name of adopter
        return self.name

    def get_desired_species(self):
        # return desired species
        return self.desired_species

    def get_score(self, adoption_center):
        # return score of "how good of a fit the specific adopter is to the specific adoption center". Formula: 1 * species in spesified adoption center
        score = float(adoption_center.get_number_of_species(self.desired_species))
        return score



class FlexibleAdopter(Adopter,object):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        # return score of "how good of a fit the specific adopter is to the specific adoption center". Formula: adopter_score + 0.3 * num_other
        score = float(adoption_center.get_number_of_species(self.desired_species))
        for species in self.considered_species:
            score += 0.3 * adoption_center.get_number_of_species(species)
        return score

class FearfulAdopter(Adopter,object):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        # return score of "how good of a fit the specific adopter is to the specific adoption center". Formula: adopter_score - 0.3 * num_feared
        score = float(adoption_center.get_number_of_species(self.desired_species)) - 0.3 * adoption_center.get_number_of_species(self.feared_species)
        if score < 0: score = 0.0
        return score


class AllergicAdopter(Adopter,object):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species[:]

    def get_score(self, adoption_center):
        for s in self.allergic_species:
            if adoption_center.get_number_of_species(s) > 0:
                return 0.0
        
        species = self.get_desired_species()
        num_desired = adoption_center.get_number_of_species(species)
        return 1.0 * num_desired


class MedicatedAllergicAdopter(AllergicAdopter,object):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.allergic_species = allergic_species[:]
        self.medicine_effectiveness = medicine_effectiveness.copy()

    def get_score(self, adoption_center):
        effects = []
        for s in self.medicine_effectiveness:
            if adoption_center.get_number_of_species(s) > 0:
                effects.append(self.medicine_effectiveness[s])
        if len(effects) > 0:
            lowest_effectiveness = min(effects)
        else:
            lowest_effectiveness = 1.0
        species = self.get_desired_species()
        num_desired = adoption_center.get_number_of_species(species)
        return 1.0 * num_desired * lowest_effectiveness

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = (location[0] * 1.0, location[1] * 1.0)

    def get_linear_distance(self, to_location):
        x1, y1 = self.location
        x2, y2 = to_location
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def get_score(self, adoption_center):
        species = self.get_desired_species()
        num_desired = adoption_center.get_number_of_species(species)

        ad_cent_location = adoption_center.get_location()
        dist = self.get_linear_distance(ad_cent_location)

        if dist <= 1:
            return 1.0 * num_desired
        elif dist <= 3:
            return random.uniform(0.7, 0.9) * num_desired
        elif dist <= 5:
            return random.uniform(0.5, 0.7) * num_desired
        elif dist > 5:
            return random.uniform(0.1, 0.5) * num_desired


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    ranking = []

    for ac in list_of_adoption_centers:
        ranking.append([ac, adopter.get_score(ac)])

    # Sort by score first, in case of duplicates - sort by center's name
    ranking = sorted(ranking, key=lambda x: x[0].get_name())
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
    return [ac[0] for ac in ranking]

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    ranking = []

    for ad in list_of_adopters:
        ranking.append([ad, ad.get_score(adoption_center)])

    # Sort by score first, in case of duplicates - sort by adopters's name
    ranking = sorted(ranking, key=lambda x: x[0].get_name())
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
    return [x[0] for x in ranking[0:n]]
