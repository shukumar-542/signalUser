import django
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete


#LOGGED_IN 

@receiver(user_logged_in, sender=User)
def login_success(sender,request,user,**kwargs):
      print('---------------')
      print('vdgfudgfidh')
      print('loggedin singnal run intro...')
      print('sender:', sender)
      print('request:', request)
      print('user:', user)
      print(f'kwarg{kwargs}')

# user_logged_in.connect(login_success,sender=User)


@receiver(user_logged_out, sender=User)
def logout_success(sender,request,user,**kwargs):
      print('---------------')
      print('Logged out intro....')
      print('sender:', sender)
      print('request:', request)
      print('user:', user)
      print(f'kwarg{kwargs}')

# user_logged_out.connect(logout_success,sender=User)


@receiver(user_login_failed)
def login_failed(sender,request,credentials,**kwargs):
      print('---------------')
      print('Logged in failde  intro....')
      print('sender:', sender)
      print('request:', request)
      print('creandatial:', credentials)
      print(f'kwarg{kwargs}')

# user_logged_out.connect(logout_success,sender=User)

@receiver(pre_save, sender=User)
def at_beganing_save(sender,instance,**kwargs):
      print('---------------')
      print('Pre save intro....')
      print('new recorde')
      print('sender:', sender)
      print('instance :', instance)
      print(f'kwarg{kwargs}')


@receiver(post_save, sender=User)
def at_beganing_save(sender,instance,created,**kwargs):
      if created:
            print('---------------')
            print('Post  save intro....')
            print('sender:', sender)
            print('instance :', instance)
            print(f'kwarg{kwargs}')
      else:
            print('---------------')
            print('Post  save intro....')
            print('update')
            print('sender:', sender)
            print('instance :', instance)
            print(f'kwarg{kwargs}')


@receiver(pre_delete, sender=User)
def at_pre_delete(sender,instance,**kwargs):
      print('---------------')
      print('Pre deletee intro....')
      print('sender:', sender)
      print('instance :', instance)
      print(f'kwarg{kwargs}')


@receiver(post_delete, sender=User)
def at_post_delete(sender,instance,**kwargs):
      print('---------------')
      print('post  deletee intro....')
      print('sender:', sender)
      print('instance :', instance)
      print(f'kwarg{kwargs}')


