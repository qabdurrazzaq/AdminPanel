from django import forms
# from django.contrib.auth import get_user_model
from .models import User

# User = get_user_model()

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'first_name',
            'mobile_no', 
            'dept_name',
            'age',
            'address',
            'add_user',
            'del_user',
            'view_user',
            'edit_user',
            'user_stats',
        )
        
        help_texts = {
            'username': None,
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_count = User.objects.filter(username = username).count()
        if user_count > 0:
            raise forms.ValidationError("Username already registered")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email = email).count()
        if user_count > 0:
            raise forms.ValidationError("Email already registered")
        return email
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name
    
    def clean_mobile_no(self):
        mobile_no = self.cleaned_data.get('mobile_no')
        return mobile_no
    
    def clean_dept_name(self):
        dept_name = self.cleaned_data.get('dept_name')
        return dept_name
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        return age
    
    def clean_address(self):
        address = self.cleaned_data.get('address')
        return address
    
    def clean_add_user(self):
        add_user = self.cleaned_data.get('add_user')
        return add_user
    
    def clean_del_user(self):
        del_user = self.cleaned_data.get('del_user')
        return del_user
    
    def clean_view_user(self):
        view_user = self.cleaned_data.get('view_user')
        return view_user
    
    def clean_edit_user(self):
        edit_user = self.cleaned_data.get('edit_user')
        return edit_user
    
    def clean_user_stats(self):
        user_stats = self.cleaned_data.get('user_stats')
        return user_stats

    def save(self, commit = True):
        user = super(AddUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.email = self.cleaned_data['email']
        user.mobile_no = self.cleaned_data['mobile_no']
        user.first_name = self.cleaned_data['first_name']
        user.dept_name = self.cleaned_data['dept_name']
        user.age = self.cleaned_data['age']
        user.add_user = self.cleaned_data['add_user']
        user.del_user = self.cleaned_data['del_user']
        user.view_user = self.cleaned_data['view_user']
        user.edit_user = self.cleaned_data['edit_user']
        user.user_stats = self.cleaned_data['user_stats']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Name'})
        self.fields['mobile_no'].widget.attrs.update({'class' : 'form-control','placeholder' : '9999-9999-99'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Email@example.com'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Password'})
        self.fields['dept_name'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Department'})
        self.fields['age'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Age'})
        self.fields['address'].widget.attrs.update({'class':"form-control", 'placeholder':"Address"})
        self.fields['add_user'].widget.attrs.update({'type':'checkbox','value':'True'})
        self.fields['del_user'].widget.attrs.update({'value':'True'})
        self.fields['view_user'].widget.attrs.update({'value':'True'})
        self.fields['edit_user'].widget.attrs.update({'value':'True'})
        self.fields['user_stats'].widget.attrs.update({'value':'True'})

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("*No data found for the username")
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("*Invalid Password")
        elif user is None:
            pass
        else:
            return password

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control'})