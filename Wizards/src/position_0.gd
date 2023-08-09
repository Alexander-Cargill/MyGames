extends Node2D

func free_sprite_children(): 
	 for child in get_children(): 
		 if child.get_class() == "Sprite": 
			 child.queue_free() 
