user_info={
          'name':'Monjur Hasan Milton',
          'age' :24,
          'occupation':'Student'
}

print(user_info)
user_info['favorite_song']=['alo alo','maya lagaise']
print(user_info)

#pop_item=user_info.pop('favorite_song')
#print(user_info)
more_info={
            
            'name'   :"Miltu",
            'City'   :"Dhaka",
            'movies' :['3 idiotes','charli','Ratsasan'] 
}

user_info.update(more_info)
print(user_info)