from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.template.loader import get_template

from django.core.mail import EmailMessage
from django.template import Context


from wsglobal.forms import ContactsForm

from wsglobal.models import Site,SiteInfo,Message

from django.core.exceptions import ObjectDoesNotExist


def cover(request):
    return render_to_response('cover.html', {})


def index(request):
    try:
        siteinfo = SiteInfo.objects.get(site=Site.objects.get(name='ColdLands'))
    except ObjectDoesNotExist:
        siteinfo = None

    return render_to_response('index.html', {
        'siteinfo': siteinfo,
    })


def contacts(reqest):
    form_class = ContactsForm

    if reqest.method == 'POST':
        form = form_class(data=reqest.POST)

        if form.is_valid():
            contact_name = reqest.POST.get('name', '')
            contact_email = reqest.POST.get('email', '')
            contact_content = reqest.POST.get('content', '')

            template = get_template('contact_template.txt')

            context = Context({
                'name': contact_name,
                'email': contact_email,
                'content': contact_content,
            })

            content = template.render(context)

            email = EmailMessage(
                subject='New email from ColdLands',
                body=contact_content,
                from_email='noreply@coldlands.org',
                to=['zolotko@netcracker.com'],
                headers={'Reply-To': contact_email},
            )

            email.send()
            return redirect('contacts')

    return render(reqest,'contact.html', {
        'form': form_class,
    })