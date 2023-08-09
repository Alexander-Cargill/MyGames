extends KinematicBody2D

var speed_x = 500.0 
var velocity = Vector2.ZERO 
var direction = Vector2(1,0)

func _physics_process(delta):
	
	move_and_slide(get_velocity())
	if global_position.x > 1200: 
		queue_free()
	
func get_velocity():
	var out: Vector2
	out.y = 0 
	out.x = direction.x * speed_x
	return out
