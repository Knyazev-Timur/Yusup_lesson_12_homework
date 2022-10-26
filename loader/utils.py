def save_picture(picture):
    filename = picture.filename

    picture.save(f'./uploads/images/{filename}')
    path = f'/uploads/images/{filename}'

    return path
