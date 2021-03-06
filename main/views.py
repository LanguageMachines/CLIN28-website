
import os

from django.shortcuts import render

def home(request):

    if os.environ["UNDER_CONST"] == 'True':
        request = render(request, 'under_construction.html', {})
    else:
        available_pdfs = [pdf_file.split('.pdf')[0] \
                                for pdf_file in os.listdir('static/on-program') \
                                if pdf_file.endswith('.pdf')]
        request = render(request, 'base.html', {
            'title': 'Computational Linguistics in the Netherlands',
            'keys': 'CLIN28, CLIN 28, Computational Linguistics in the Netherlands, Nijmegen',
            'available_pdfs': available_pdfs
        })

    return request

def dates(request):
    return render(request, 'dates.html', {
        'title': 'Important Dates',
        'keys': 'CLIN28, CLIN 28, Important dates',
    })

def calls(request):
    return render(request, 'calls.html', {
        'title': 'Calls',
        'keys': 'CLIN28, CLIN 28, calls, abstracts',
    })

def shared_task(request):
    return render(request, 'shared_task.html', {
        'title': 'Shared task',
        'keys': 'CLIN28, CLIN 28, shared task, shared task call',
    })

def thesis_prize(request):
    return render(request, 'stil_thesis_prize.html', {
        'title': 'Thesis prize',
        'keys': 'CLIN28, CLIN 28, thesis prize, best thesis',
    })

def posters(request):

    # Convert pdf to png;
    # for i in $( ls *.pdf); do convert -verbose -density 150 -trim $i -quality 100 -flatten -sharpen 0x1.0 thumbnails/$i.png; done
    # Resize the png;
    # for i in $( ls thumbnails/*.png); do convert -geometry x200 $i $i; done

    poster_paths = sorted([{'thumbnail': 'posters/thumbnails/' + poster + '.png',
                            'original': 'posters/' + poster} \
                           for poster in os.listdir('static/posters') \
                           if poster.endswith('.pdf')],
                          key=lambda k: k['original'])

    return render(request, 'posters.html', {
        'title': 'Gallery',
        'keys': 'CLIN28, CLIN 28, posters, display posters, dowload posters',
        'poster_paths': poster_paths,
    })

def photos(request):

    # Create the thumbnails (install imagemagick)
    # for i in $( ls *.jpg); do convert -geometry x200 $i thumbnails/$i; done

    photo_paths = sorted([{'thumbnail': 'images/photos/thumbnails/' + photo,
                           'original': 'images/photos/' + photo} \
                          for photo in os.listdir('static/images/photos') \
                          if photo.endswith('.jpg')],
                         key=lambda k: k['original'])

    return render(request, 'photos.html', {
        'title': 'Gallery',
        'keys': 'CLIN28, CLIN 28, photos, photo gallery',
        'photo_paths': photo_paths,
    })

def presentations(request):

    # Convert pdf to png;
    # for i in $( ls *.pdf); do convert -verbose -density 150 -trim $i[0] -quality 100 -flatten -sharpen 0x1.0 thumbnails/$i.png; done
    # Resize the png;
    # for i in $( ls thumbnails/*.png); do convert -geometry x200 $i $i; done

    presentations_paths = sorted([{'thumbnail': 'presentations/thumbnails/' + poster + '.png',
                                   'original': 'presentations/' + poster} \
                                  for poster in os.listdir('static/presentations') \
                                  if poster.endswith('.pdf')],
                                 key=lambda k: k['original'])

    return render(request, 'presentations.html', {
        'title': 'Gallery',
        'keys': 'CLIN28, CLIN 28, presentations, presentation gallery',
        'presentations_paths': presentations_paths,
    })
