from bs4 import BeautifulSoup
import requests

page_num = 1
current_page = 0
indiv_post_url = []


def pagination(page_num):
    page = []
    for ultags in soup.find_all('ul', class_='lia-paging-full-pages'):
        for litag in ultags.find_all('a'):
            page.append(int(litag.text))

        if max(page) > page_num:
            return max(page)
        else:
            break


while True:
    url = 'https://community.withairbnb.com/t5/forums/searchpage/tab/message?q=party%20bans&page=' + \
        str(page_num) + '&collapse_discussion=true&search_type=thread'
    url_text = requests.get(url).text
    soup = BeautifulSoup(url_text, 'lxml')
    current_page = page_num
    page_num = pagination(current_page)

    messages = soup.find_all('div',
                             class_='MessageView lia-message-view-message-search-item lia-message-view-display lia-row-standard-unread lia-thread-topic')
    for message in messages:
        data = message.find('h3', class_='message-subject').text
        hyperlink = message.find('a', class_='page-link lia-link-navigation lia-custom-event')['href']

        message_subject = data.replace('\n', '').replace('\t', '').replace('\r', '')
        hyperlink = 'https://community.withairbnb.com/' + hyperlink


        posted_date = message.find('span', class_='local-date').text
        latest_post_time = message.find('div', class_='MessageLastReply lia-component-latest-reply').text
        post_type = message.find('a',
                                 class_='lia-link-navigation lia-message-board-link lia-component-common-widget-link')
        if message.find('div',
                        class_='search-item-stats lia-message-item-metadata lia-message-item-metadata-main') is not None:
            reply_count = message.find('span', class_='MessageRepliesCount lia-component-replies-count').text
        else:
            reply_count = '0'

        tags = []
        for ultags in message.find_all('ul', class_='lia-list-standard-inline'):
            for litag in ultags.find_all('li'):
                tags.append(litag.text)

            post_date = posted_date.replace('\n', '').replace('\n', '').replace('\t', '').replace('\r', '')
            replied_count = reply_count.replace('\n', '').replace('\t', '').replace('\r', '').split(' ')[0]
            message_subject = data.replace('\n', '').replace('\t', '').replace('\r', '')
            post_type1 = post_type.text.replace('\n', '').replace('\t', '').replace('\r', '')
            hyperlink = 'https://community.withairbnb.com/' + hyperlink
            print(f"{post_type1} ## {post_date} ## {replied_count} ## {message_subject} ## {tags} ## {hyperlink}")

            indiv_post_url.append(hyperlink)


    try:
        if current_page < page_num:
            continue
        else:
            break
    except TypeError:
        break

print(indiv_post_url)
print("Exiting the While Loop")
