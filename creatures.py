import sqlite3
import random

class Creature:
    def __init__(self, name, scientific_name, habitat, drops, attack, defense, health, speed, ability, catagory,moves, sprite, rarity, description):
        self.name = name
        self.scientific_name = scientific_name
        self.habitat = habitat
        self.drops = drops
        self.attack = attack
        self.defense = defense
        self.health = health
        self.ability = ability
        self.speed = speed
        self.catagory = catagory
        self.moves = moves
        self.sprite = sprite
        self.rarity = rarity
        self.description = description
        self.atkbuff=1
        self.defbuff=1

def creature_coverter(scientific_name):
    conn = sqlite3.connect('Organisms.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Animals WHERE scientific_name = ?", (scientific_name,))
    row = cursor.fetchone()
    conn.close()
    creature= Creature(
        name=row[0],
        scientific_name=row[1],
        habitat=row[2],
        drops=row[3],
        attack=row[4],
        defense=row[5],
        health=row[6],
        speed=row[7],
        ability=random.choice(row[8].split(',')),
        catagory=row[9],
        moves=row[10].split(','),
        sprite=row[11],
        rarity=row[12],
        description=row[13]
    )
    return creature

def spawn_random_creature(habitat):
    habitat = habitat.title()
    conn = sqlite3.connect('Organisms.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT scientific_name, rarity
    FROM Animals
    WHERE habitat LIKE ?
""", (f'%{habitat}%',))
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        return None
    rarity_weights = {
        "Common": 60,
        "Uncommon": 25,
        "Rare": 10,
        "Legendary": 5
    }
    creatures = [row[0] for row in rows]
    weights = [rarity_weights.get(row[1], 1) for row in rows]
    random_scientific_name = random.choices(creatures, weights=weights, k=1)[0]
    return creature_coverter(random_scientific_name)

creature1 = spawn_random_creature('urban')
creature2 = spawn_random_creature('urban')
print(creature1.name)
print(creature2.name)
    
