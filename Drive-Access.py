import gdata.docs.service

client = gdata.docs.service.DocsService()
client.ClientLogin(username='cisnerosa@milton.k12.wi.us',password='t44p+Eer;4')

documents_feed = client.GetDocumentListFeed()

for document_entry in documents_feed.entry:
  print document_entry.title.text
