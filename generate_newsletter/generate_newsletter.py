#!/usr/bin/env python3
import pprint
from datetime import datetime

WORKSHOP_HTML_BLOCK_PRE = '''
<!--[if mso]>
<style>#list-r1c0m1 ul {
    margin: 0 !important;
    padding: 0 !important;
}

#list-r1c0m1 ul li {
    mso-special-format: bullet;
}

#list-r1c0m1 .levelOne li {
    margin-top: 0 !important;
}

#list-r1c0m1 .levelOne {
    margin-left: -20px !important;
}

#list-r1c0m1 .levelTwo li {
    margin-top: 0 !important;
}

#list-r1c0m1 .levelTwo {
    margin-left: 10px !important;
}

#list-r1c0m1 .levelThree li {
    margin-top: 0 !important;
}

#list-r1c0m1 .levelThree {
    margin-left: 40px !important;
}

#list-r1c0m1 .levelFour li {
    margin-top: 0 !important;
}

#list-r1c0m1 .levelFour {
    margin-left: 70px !important;
}

#list-r1c0m1 .levelFive li {
    margin-top: 0 !important;
}

#list-r1c0m1 .levelFive {
    margin-left: 100px !important;
}

#list-r1c0m1 .levelSix li {
    margin-top: 0 !important;
}

#list-r1c0m1 .levelSix {
    margin-left: 130px !important;
}

#list-r1c0m1 .levelSeven li {
    margin-top: 0 !important;
}

#list-r1c0m1 .levelSeven {
    margin-left: 160px !important;
}</style><![endif]-->
'''

WORKSHOP_HTML_BLOCK = '''
<table border="0" cellpadding="15" cellspacing="0" class="list_block block-2"
       id="list-r1c0m1" role="presentation"
       style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;"
       width="100%">
    <tr>
        <td class="pad">
            <div class="levelOne" style="margin-left: 0;">
                <ul class="leftList" style="margin-top: 0; margin-bottom: 0; padding: 0; padding-left: 20px; color: #101112; direction: ltr; font-family: Helvetica Neue,Helvetica,Arial,sans-serif; font-size: 20px; font-weight: 700; letter-spacing: 0; line-height: 120%; text-align: left; list-style-type: disc;">
                    <li style="margin-bottom: 1px; text-align: left;">{}</li>
                </ul>
            </div>
            <div class="levelTwo" style="margin-left: 30px;">
                <ul class="leftList" style="margin-top: 0; margin-bottom: 0; padding: 0; padding-left: 20px; color: #101112; direction: ltr; font-family: Helvetica Neue,Helvetica,Arial,sans-serif; font-size: 20px; font-weight: 700; letter-spacing: 0; line-height: 120%; text-align: left; list-style-type: circle;">
                    {}
                </ul>
            </div>
        </td>
    </tr>
</table>
'''

SUBTEXT_HTML = '<li style="margin-bottom: 1px; text-align: left;"><sub>{}</sub></li>'
TICKET_LINK_HTML = '<a href="{}" style="text-decoration: underline; color: #eb6b09;">{}</a>'

WORKSHOP_DATA = [
    {
        'title': 'Coding im Dojo am 28.10.2023',
        'subtexts': [
            'Freies Programmieren und ein wenig Inspiration :)'
        ],
        'tickets': {
            'text': 'Tickets wie immer unter {}',
            'link': 'https://pretix.eu/dojosw/'
        }
    },
    {
        'title': 'Workshop am 11.11.2023',
        'subtexts': [
            'Was wir genau machen wissen wir noch nicht, aber wird bestimmt cool :D'
        ],
        'tickets': {
            'text': 'Tickets wie immer unter {}',
            'link': 'https://pretix.eu/dojosw/'
        }
    }
]

WEEKDAYS = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']


def main():
    html_workshops = []
    for workshop in WORKSHOP_DATA:
        html_subtext = []
        for subtext in workshop['subtexts']:
            html_subtext.append(SUBTEXT_HTML.format(subtext))
        ticket_subtext = SUBTEXT_HTML.format(workshop['tickets']['text'].format(TICKET_LINK_HTML.format(workshop['tickets']['link'], workshop['tickets']['link'])))
        html_subtext.append(ticket_subtext)
        html_workshop = WORKSHOP_HTML_BLOCK.format(workshop['title'], '\n'.join(html_subtext))
        html_workshop = '\n'.join([WORKSHOP_HTML_BLOCK_PRE, html_workshop])
        html_workshops.append(html_workshop)

    html_workshops = '\n'.join(html_workshops)

    today = datetime.today()
    weekday = '{}, {}.{}.{}'.format(WEEKDAYS[today.weekday()], today.day, today.month, today.year)

    # load template
    with open('template_eltern_newsletter.html', 'r') as f:
        template_content = f.read()
    template_content = template_content.replace('WORKSHOPS', html_workshops)
    template_content = template_content.replace('WEEKDAY', weekday)

    with open('eltern_newsletter.html', 'w') as f:
        f.write(template_content)


if __name__ == '__main__':
    main()

