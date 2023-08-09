extends KinematicBody2D
class_name Player

const DEFAULT_KEY_STATE  = 5
const DEFAULT_COMBO_VALUE = [0,0,0,0]

var spell_state 
enum {SPELL_FAILED, STONE_ACTIVATED, SPELL_CAST} 

var speed_x = 400.0
var speed_y = 250.0
var acceleration = 0
var direction = Vector2.ZERO
var velocity = Vector2.ZERO setget set_velocity, get_velocity

func set_velocity(vel): 
	velocity.x = vel  
	
func get_velocity(): 
	return velocity

var combo_key = DEFAULT_KEY_STATE
var combo_sequence = DEFAULT_COMBO_VALUE setget combo_sequence_set, combo_sequence_get
var combo_index = 0
var combo_success = false 

func combo_sequence_set(arr): 
	combo_sequence = arr 

func combo_sequence_get(): 
	return combo_sequence


func get_spell() -> Array: 
	randomize()
	var arr = [0,0,0,0] 
	for i in range(4):
		arr[i] = randi()%4 + 1 
	
	return arr 

	

