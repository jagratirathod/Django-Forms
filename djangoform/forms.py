from django import forms

class Signupform(forms.Form):
    email=forms.CharField(label='Email :',widget=forms.TextInput(
        attrs={
            'class':'form-control-label' ,
            'placeholder':'enter username'
        }
    )
    )

    password=forms.CharField(label='Password :',widget=forms.PasswordInput(
        attrs={
            'class':'form-control-label' ,
            'placeholder':'enter password'
        }
    )
    )

    firstname=forms.CharField(label='First name :',widget=forms.TextInput(
        attrs={
            'class':'form-control-label' ,
            'placeholder':'enter firstname'
        }
    )
    )

    lastname=forms.CharField(label='Last name :',widget=forms.TextInput(
        attrs={
            'class':'form-control-label' ,
            'placeholder':'enter lastname'
        }
    )
    )

    mobile=forms.CharField(label='Mobile number :',widget=forms.TextInput(
        attrs={
            'class':'form-control-label' ,
            'placeholder':'enter mobile number'
        }
    )
    )

    married=forms.BooleanField(label='Married',required=False)
    unmarried=forms.BooleanField(label='UnMarried',required=False)
    


    gender=forms.ChoiceField(label="Select Gender :",choices=[('M','male'),('F','female')],widget=forms.RadioSelect(
        attrs={
            'class':'form-control-label' 

        }
    ))

    
    game=forms.CharField(label='Select Games :',widget=forms.Select(choices=[('F','football'),('C','cricket'),('V','volleyball')],
        attrs={
            'class':'form-control-label'
        }
    ))

    
    file = forms.FileField(label="File") 

    image = forms.ImageField(label="Upload Your PHOTO here")


  

    
class Loginform(forms.Form):
    email=forms.CharField(label='Email :')       
    password=forms.CharField(label='Password :')
