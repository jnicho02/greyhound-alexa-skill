#  app logic works completely separate to Alexa code

def can_eat(food):
    things_a_dog_can_eat = [
        'banana',
        'cheese',
        'dog food',
        'kibbles',
        'yoghurt'
    ]
    things_a_dog_shouldnt_eat = {
        'apple' : 'The seeds contain cyanogenic glycosides which can result in cyanide poisoning.',
        'apricot' : 'The stone contains cyanogenic glycosides which can cause cyanide poisoning.',
        'baby food' : 'check the ingredients to see if it contains onion powder, which can be toxic to dogs.',
        'broccoli' : 'Broccoli contains isothiocynate. While it may cause stomach upset it probably won\'t be very harmful unless the amount fed exceeds 10% of the dogs total daily diet.',
        'candy' : 'Sugarless candy containing xylitol can be a risk to pets',
        'cat food' : 'Cat food is generally too high in protein and fats and is not a balanced diet for a dog.',
    }
    things_a_dog_mustnt_eat = {
        'alcohol' : 'Ingestion can lead to injury, disorientation, sickness, urination problems or even coma or death',
        'anti-freeze' : 'It can be deadly',
        'avocado' : 'Avocado contains a toxic element called persin which can damage heart, lung and other tissue in many animals.',
        'bones' : 'Cooked bones can be very hazardous for your dog. Bones become brittle when cooked which causes them to splinter when broken. Especially bad bones are turkey and chicken legs, ham, pork chop and veal.',
        'bread dough' : 'your dog\'s body heat causes the dough to rise in the stomach which may give it bloat',
        'caffeine' : 'Caffeine is a stimulant and can accelerate your pet\'s heartbeat to a dangerous level. Pets ingesting caffeine have been known to have seizures, some fatal.',
        'cherries' : 'Cherry stone contains cyanogenic glycosides which can cause cyanide poisoning.',
        'chocolate' : 'Chocolate contains a cardiac stimulant and a diuretic. An overdose can increase the dog’s heart rate or may cause the heart to beat irregularly. Death is quite possible, especially with exercise.',
    }
    say = "I don't know about {} so cannot comment".format(food)
    if food in things_a_dog_mustnt_eat:
        say = "No, a dog must not eat {}. {}".format(food, things_a_dog_mustnt_eat[food])
    if food in things_a_dog_shouldnt_eat:
        say = "A dog should not eat {}. {}".format(food, things_a_dog_shouldnt_eat[food])
    elif food in things_a_dog_can_eat:
        say = "Yes, a dog can eat {}.".format(food)
    return say
