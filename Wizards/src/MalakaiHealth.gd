extends ProgressBar

func LoseHealth():
	self.value -= 10
	if self.value <= 0: 
		get_node("Label").visible = true 
		yield(get_tree().create_timer(3), "timeout")
		get_node("Label").visible = false 
		get_tree().reload_current_scene()
		
