from django import forms

from .models import Genre

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            "title","category"
        ]

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = [
            "title","category"
        ]

        for data in fields:
            self.fields[data].widget.attrs.update(
                            {
                                "type":"text",
                                "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 outline-none"
                            }
                        )

class UpdateGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = [
            "title","category"
        ]

    def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            fields= [
                "title","category"
            ]
            for data in fields:
                self.fields[data].widget.attrs.update(
                    {
                        "type":"text", "name":"author", 
                        "required class":"w-full px-4 py-2.5 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:bg-white outline-none transition-all"
                    }
                )
