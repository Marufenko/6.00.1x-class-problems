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
        self.location = location

    def get_number_of_species(self, animal):
        # return number of apecified animal in adoption center
        return self.species_types[animal]

    def get_location(self):
        # return location of adoption center
        self.float_location = (float(self.location[0]), float(self.location[1]))
        return self.float_location

    def get_species_count(self):
        # return dict of available pets in adoption center
        self.dict_copy = self.species_types.copy()
        for key in self.dict_copy.keys():
            if self.dict_copy[key] == 0:
                del self.dict_copy[key]
        return self.dict_copy

    def get_name(self):
        # return name of adoption center
        return self.name

    def adopt_pet(self, species):
        # update the value for specified pet on "-1" value
        if self.species_types[species] > 0:
            self.species_types[species] = self.species_types[species] - 1


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
        self.score = float(1 * adoption_center.get_number_of_species(self.desired_species))
        return self.score



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
        self.num_other = 0.0
        for species in self.considered_species:
            self.num_other = adoption_center.get_number_of_species(species)
        self.score = super(FlexibleAdopter, self).get_score(adoption_center) + float(0.3 * self.num_other)
        return self.score

# НЕДОДЕЛАН!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
        score = super(FearfulAdopter, self).get_score(adoption_center) - 0.3 * adoption_center.get_number_of_species(self.feared_species)
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
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        #an AllergicAdopter will return a value that is 0 if the adoption center has one or more of a species that the adopter is allergic to, otherwise it should calculate score based on the Adopter's calculate score method.
        for element in self.allergic_species:
            if adoption_center.get_number_of_species(element) > 0:
                return 0.0
        score = super(AllergicAdopter, self).get_score(adoption_center)
        return score


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
        self.medicine_effectiveness = medicine_effectiveness

#get_number_of_species(self, animal)

    def get_score(self, adoption_center):
        tmp = {} #словать со всеми алергенными
        tmp_list = []
        for pet in self.medicine_effectiveness:
            if adoption_center.get_number_of_species(pet)>0:
                tmp[pet] = self.medicine_effectiveness[pet]

        if tmp == {}:
            score = super(MedicatedAllergicAdopter, self).get_score(adoption_center)
            return score
        else:
            tmp_list = tmp.values().sort()
            score = tmp_list[0] * super(MedicatedAllergicAdopter, self).get_score(adoption_center)
            return score

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
    # Your Code Here, should contain an __init__ and a get_score method.


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here
