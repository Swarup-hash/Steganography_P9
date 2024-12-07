from stegano import lsb
secret = lsb.hide("A_visually_appealing_abstract_design_with_a_subtle.png", "Swarup")
secret.save("steganography_image.png")
