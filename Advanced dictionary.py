my_skill = {
    'html':{
    'main':'52%',
    'sass':'55%'
    },
    'css':{
    'main':'77%',
    'sass':'59%'

    },
}
for main_key,main_value in my_skill.items():
    print(f'{main_key}Progress Is : ')
    for child_key,child_value in main_value.items():
        print(f'-{child_key}>>>{child_value}')