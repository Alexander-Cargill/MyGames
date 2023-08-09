extends "./player.gd"

onready var anim = get_node("AnimationMalakai")
export var Fireball: PackedScene 

signal spell_hit 

func _ready(): 
	connect("spell_hit", get_parent().get_node("MalakaiHealth"), "LoseHealth")

func _on_RechargeTimer_timeout():
	 combo_sequence = get_spell()
	 stone_display(combo_sequence)
	 print(combo_sequence)
	
func _on_Area2D_body_entered(body):
	acceleration = -10000
	body.queue_free() 
	anim.play("spell_hit_malakai")
	emit_signal("spell_hit")
	
func _physics_process(delta):
	 move(velocity, delta)
	 direction = get_direction() 
	 velocity = calculate_velocity(direction, acceleration, delta)
	 if acceleration < 0 : 
		 acceleration += 150
	 else: 
		 acceleration = 0
		

func get_direction():
	var out = Vector2.ZERO 
	out.x = Input.get_action_strength("Malakai_move_right") - Input.get_action_strength("Malakai_move_left") 
	out.y = Input.get_action_strength("Malakai_move_down") - Input.get_action_strength("Malakai_move_up") 
	return out 

func calculate_velocity(dir: Vector2, acc: int, delta): 
	var out = Vector2.ZERO
	
	out.x = dir.x * speed_x 
	out.y = dir.y * speed_y
	
	out.x += acc * delta
	
	return out

func move(vel, delta): 
	
	if global_position.x < 80:
		global_position.x = 80
	
	
	if global_position.y > (global_position.x)*(-5.14) + 2399:
		global_position.x = (global_position.y-2399)/(-5.14)
		
	if global_position.y < 290:
		global_position.y = 290
	if global_position.y > 500:
		global_position.y = 500
	
	global_position.x += vel.x * delta
	global_position.y += vel.y * delta
		 
	

func _process(delta): 
	combo_key = input_handler()
	if combo_sequence != DEFAULT_COMBO_VALUE: 
		combo_index = check_spell(combo_sequence, combo_index, combo_key)
	 
func stone_display_clear():
	for i in range(len(DEFAULT_COMBO_VALUE)):
		for child in get_node("Stones/position_"+str(i)).get_children(): 
			if child.get_class() == "Sprite": 
				 child.set_modulate("fd0e10")
			if child.get_class() == "AnimationPlayer":
				 child.play("stone_fade")
		
func stone_display(sequence: Array): 
	
	for i in len(sequence): 
		if sequence[i] == 1:
			var stone1 = Sprite.new()
			stone1.set_texture(load("./assets/Malakai/stone_U.png"))
			var nodepath = "Stones/position_"+str(i) 
			get_node(nodepath).add_child(stone1)
		elif sequence[i] == 2:
			var stone2 = Sprite.new()
			stone2.set_texture(load("./assets/Malakai/stone_H.png"))
			var nodepath = "Stones/position_"+str(i) 
			get_node(nodepath).add_child(stone2)
		elif sequence[i] == 3:
			var stone3 = Sprite.new()
			stone3.set_texture(load("./assets/Malakai/stone_J.png"))
			var nodepath = "Stones/position_"+str(i) 
			get_node(nodepath).add_child(stone3)
		elif sequence[i] == 4:
			var stone4 = Sprite.new() 
			stone4.set_texture(load("./assets/Malakai/stone_K.png"))
			var nodepath = "Stones/position_"+str(i) 
			get_node(nodepath).add_child(stone4)
		
				
			
func check_spell(combo_sequence: Array, combo_index: int, key: int): 
	if combo_index >= 4: 
		print("spell_cast")
		anim.queue("cast_attack_spell")
		self.set_modulate("ffffff")
	
		combo_sequence_set(DEFAULT_COMBO_VALUE)
		combo_index = 0
		get_node("RechargeTimer").start() 

	if combo_sequence[combo_index] == key: 
		get_node("Stones/position_"+str(combo_index)+"/anim_player").play("stone_fade")
		combo_index += 1 
		
		print(combo_index)
		
	elif  key < DEFAULT_KEY_STATE : 
		print("spell_fail")
		combo_sequence_set(DEFAULT_COMBO_VALUE)
		stone_display_clear()
		combo_index = 0
		get_node("RechargeTimer").start() 
	
	return combo_index 
	
func input_handler() -> int: 
	
	if Input.is_action_just_pressed("Malakai_combokey_U"):
		print("test1")
		return 1
		
	if Input.is_action_just_pressed("Malakai_combokey_H"): 
		print("test2")
		return 2
		
	if Input.is_action_just_pressed("Malakai_combokey_J"):
		print("test3")
		return 3 
		
	if Input.is_action_just_pressed("Malakai_combokey_K"):
		print("test4")
		return 4
	 
	return DEFAULT_KEY_STATE 
		
	
func cast_fireball(): 
		var fireball = Fireball.instance() 
		fireball.global_position = self.global_position
		fireball.set_collision_layer(16)
		get_parent().add_child(fireball)
		get_parent().move_child(fireball, 0)
		acceleration = -10000   # Knockback
		
	 
		



