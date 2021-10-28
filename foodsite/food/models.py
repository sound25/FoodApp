from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Item(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=10000,default="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYWFRgVFhUZGRgZHBoeGBwaGhghHxwaHRwaHhoaGBwcIS4lHB4rIRoaJjgmKzAxNTU1GiQ7QDs0Py40NTEBDAwMDw8PEA8PEDEdGB0xMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMf/AABEIAOMA3gMBIgACEQEDEQH/xAAbAAACAgMBAAAAAAAAAAAAAAAABgEFAgMEB//EAEIQAAIAAwQHBgUBBQcEAwAAAAECAAMRBBIhMQUGQVFhcYEiMpGh0fATQlKxwWIUM3LC8SNDU5KisuEVJILSFlST/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/APXna9gIFe7gc4HW7iM4EW9ic4CEW7ieUBW8ajKJRr2BiGYqaDKAlmvYDnArXRQ5+sDLdxHKBVqLxzgBFu4mIZLxqMolGvYGIZipoMoCWa9gOcCtdFDn6wMt3EcoFWovHOAEW7iYgrU3hl6RKm9gYhiQboy9YCXN7ARKsALpz9YhxdxESqgi8c/SAhFu4mIK1N4ZekSpvYGIYkG6MvWAlzewEAagu7fWBxdxEAWoqc/SAEF3PbEFam9sz8IlDez2RBahu7MvGAl2vYCBHuihzgdbuIgRbwqc4CEW7ieUBW8bwygRr2B5wFrpujKAlmvYDnArUF05+sDrdxECrUXjn6QAi3cTAy3sRApvYGBmu4CAhUu4nygZL2I84EJbA5QMxU0GUBLG9gOeMCvdFDnA63cRnAqgipzgIVbuJ5YQFbxvDL0gU3sDlEsxBoMoAZr2A54wK90UOcDrdxECqCKnOAhVu4nlhAVvG8MvSBTewOUSzEGgygBmvYDnjArUF05+sDi7iIFUEXjn6QEKLuJ8oCtTeGXpApvYNEsxBoMoAZr2A84FagunP1gcXcRGLsoUuxApiSTQCm+AlRdxPlAVqb2z0ihmax32uSJTziNo7Kjmf6QD/qLjBZMsbASSevegL9jewGzfAGoLu3LxigWz6RXEPIbhj/6iMW0taZeM+ykja0s1Hhj94BgVbuJ8oCl43hlFfo3TUqebqtj9LdlvDb0iwZipoMoCWa9gOeMCtdFDn6wOt3EZwKoIqc4CFW7ieWEBWpvDL0gU3sGgZiDdGUBLNewHnArXcD5QOLuIgVb2JzgBmvYDzgVruB8oGULiM4EUHE5wEKt3E8sICl43hlxgQlsGyiWYg0GUAM17Ac8YFa6KHP1gcBcRnAqgipzgIVbuJ5YQFLxvDzgU3sGiWYg0GUAM17Ac8YFa6KHP1gcBcRnEqoIqc4DFVu4nlhAVqbwy9I0zbWi/vHVR+pgPvFNpTWNAtyzMHmsQqgAkAttqRQwHfpXTcmUAHY3tigVY9Bl1jhXT08jsWKYy72N3yumOzQuglki+3bnNi7nHE/TXLnnF3AK8nWZUak+VMlE71JHjGmRZ2tzmY9VsynsLkXIwq3vgN8NFokK6lXUMpzBFRCpNRrDMCqxNmmtSh+Rue77jlANMmWktQqhVUZAUET+0rv8AIxXwQFms1TkRGyKiNkucy7ajcYDXpPQMmdiVuvsdcGrx39Yq5WkJ1kIl2iryiaJNGY3B/wDnHnDLKnBhhnugtNnV1KOoKkUIMBqlEABqgqRgRjWuIPKMit43hl6QuWFmsk4WdyTJckyWPyn6SfLqDthkZiDQZQAzXsBzxgVrooc/WBxdxECqCKnOAhVu4nyiSt7EecQhvd6BiVwXKAFS7ifKBkvYjzgUk4Nl4QMxBouUBLNewHPGBXu4GBgBiufjAqgipzgIVbuJ5YQFb3aHukc9stiy0Z5lbqiuWJOQA44xTDT1oIvrY3+HnWvaI3gUgN+ktMOZnwJEu+4ALkmirXKuPEbdsabPrEZRaXaluMoqCtSGB3DH3WNWqNpEyfapgUgNcIBzHewPhBrzZyBLnLgVa6TuDYg9CD4wGm0a0sMZcoKNjzTQHktcehiktWl50ypaa7Db8MXFHNs6R0JYUHbclzmWc1jq0Poo2pr71WQpooGF8j8f0gF1EZzRELngGc9dnlF3qlZG/awJiFWRGajLdNaqoNCB9UPtms6IoVFCqNgFIX9JN8G3S5xwSanw2O5q4V/0+BgGeCCCAIpda5IayzK7AGHAgiLqFzXC1UlCSuMyaQqqM6VqTTwHWAz0bMLSkY5lFJ8BHTFDZ9MiUESdKeVQAAsppgKe6RdyZquoZWDA5EGogM4IIICUYg1EWUpwwrFZHTY3xI3wHNrJYPjSGA7y9pDtvLsHMVEGgdIfEs8tzixFG/iBofXrFvChqlapa/EklwGExrqk0qMuzsOIygGZVu4nlhAVvG9s9IFJODZeEDMQaDL3XGAlmvYDzgVruB8oGFO76wKoOLZ+EAM97AQK93AwMAMVz8Y4tKW9ZMozHFSMFGRYnIe90B2Kt3E8oCt7tCFtpmkLvxiEK5/Cp2rvQVrTj02RrmaZe1XZNmBS8tZjH5AcwD+YDZrFpAWgGyyUMxyQWIPZWh2nKO3VvTImL8FyBOl9kj6ruFVO3LGKG2zVQGyWbD/HmbWORWvvdvjlbRyhRcJVlxVhnXeYB9nTJclWdrqLmxoBU8aZmFrSGkJ1sRpciQTLb+8cgZHNR04xo0Uky2uPjmqSMCBgHfHPoMf+YdFUAUAoBlSAQrToG23Lt1GFAOywvUH8VIv9A6Xl0WzlDJdQAEbbT6TTE7YYYqdO6IWem6YuKMMCDurugLaOLSejknyzLbI4g7Q2xhxjj1b0kZ0rt/vJZuzBtqMiRx+4MXMAp2bSk2yUlWlWZBgk1ccNgb3XnnFtL1hszConp1ND4HGLNlBFCKg51hU1o0fKRrOyy0AM0K4CgBgcaNTkfGA7LVrTK7sgNOc5BQaV4kjLlGWhtFPfNptBrNPdXYi7hxjuW4nZloqD9KgV8IPjt9RgO2bKVgQyhgcwQCD0MKmktGtZG+PIqZX95LrkPqWvscsmSTatjePrHRNlhgQRUEEEbwc4Cps85XVXU1VhURnC1YNIpZjNkTCew5CUBJKn2D1jq/8AkabJU4jeEHrAXcb7GO10ijkawSGNCxQ7nBHnlF6k5JaX3dQpxvVFKbKHb0gN1utKy0eY2SqT6DqcI860e8orctCFL7FknLmpO/etR0r1ix1g0w1pIlSUd5akFiqmrEZDLARyzb9269lmBf4W9BAXMvSU2zlZdoN+USLk8Y4UwvUz+/OGSXNF0UNQRgRkQciIQtC6XRCbPN7VnbCjjFCd/D+sXAvWFxWr2Zj2WzMsnLmPvzzBmVbuJ8okrexHKMJLhwCTVSKg7DXIgxmxIwXLxgMHIQXmYAbSTTzMLetVplzZN5JiMUdWKhlJoKjIc4xNn/abZMlz2a7LAKS60DCmLefPHhFnatVbM4oEKHepNfOoMBcyJoZVYZMARyIrCXpsTLHMcysEtAoP0PXGm7M058IcJMtZUsKDREUCpOSqMyeQhYt9oe3VlSUAlKwrNeuY+j3XHZAV1kswRaDPad5jdFhL1OBHbnzCf00A86xrn6qTFFZM8k/S4wPUekB1ajAfs7HaXavgIZYQ9XNImzTJkm0D4YbtY1oGG7eCN24RlpjW13YJZqgV710FmOwKpBoPOAeoIr0tLBEDUv3Vv8GoLwHWMPjN9RgKjSQ/ZbUtoH7ub2Zu4Nsb89DvhpBistMpZ8t5TfMMDuOw8wcY49VraxRpEz95JN012r8p/HhvgGCFjXA1NmTa00H/AC4fzQzwoT56z7dQEUkIbor3n+am+lf9MBcQQQQBFhZWqo4YRXxjpXSIs8kse81Qi72OXQbYDh0Ega12t6AgMqg0GYqDTwhnha0BZ2kyqE9tyXfLM7PfGLaXaztxgOfWB5CymacisBgoIFSTkFOY5xSaC1ZDATJ4IUkskqpuqDiL1ft4x0TB+020KcZdnAYjYXNCK9f9phqgNcqWFF1VCgZAAAeAjZBBAVelNCSZ4N9aNsZaBh12jgYprC5lN+w2kBkcESm2EbFO47tx6Q2xUax6OE6QwA7adpDtvDGg55QFXolms842OY1UPakMd2PY97RxEMYN3A47YW7QDarEk5f3ssXgRneTvU50rzpFzoa1rPkpMIFSKHmMD51gOXS+iRPKujGXNTuOPs1NkckrTs2QwS1pQZCaoqrcwPx4QwMAO7nwxhd1rF79nRvnnKCDuwH80BGmrWLS8qzSXBWZ2pjKfkGNPLLlDLZ7OqKEUUVRQAQtaFsipb7QqqFVUW6N14ITTrDXAEEEaps4LnnugKzWDQy2hKYB1xVvweBhc1WtUuXNMqdLVJtbocjGv0nYDuIz+7f+2fp84pNY9EraFvoKTlGH6gPlPHdAWTZnmY5JFvlu5RHDMuYFfvkekKC6RtDqJF+jDs0PZZtl0sfmGVMKxeavaFMkl3IvkUAGSjbjtOUBeq1DWKvTqmVMl21BgKLOA2qdv4/yxZxsVFdWlsKq4II5wFZp3WJVW5Ia/McChXJQRW8eNNnjC2ujqKpViJimocfVGdms3wZryWHaU1DfUuwjpSOyAzs2n2Ts2hCP1qKg8SNnSO0afs3+L/pf/wBYrmOBjr1ZsiGzBmRGZmc1ZVJAFBQEjLCAyOsSnCRLea+zAhRz2/aMrJo12cT7Q15/lUd1N1OPvGLVVAwAAHCJgCIZgBU5DE8oGYAEk0AxJOwRRgz7beWXRJFaM5zfeF99dkB3anKWE6d/iTDTiFr6mGCbOC890YWKyrKRZa4KooPyTxJqY45j1JMBsa0sdtOUC2hht8Y0wQFjJnhuBjdFUjUNRHfOmUVm3KT4CsBQal/u5q7FnOByosa9XJVydabNWgVgyD9Lf8XfGN2pK/8AbXjmzsTxOX4jktswy7e5XNpKk/5gP5YBmCXcc4XNbpgBsz7poPhQ/iGNa/NlxhV19HYl0yvHxuwHVpN/gW2XPOCTVuOdx2E/6egMNEU1nRLXZUDYhlFd4dcCRxBBhY0taLXZ0Eh3IXJJi/Mv0k5qR4884Bh0trPKkPcoXYd67Si8DvPCOi/e7W/GFDQerTTaTHICZ4EEvTZgcOuMN4EAQAxyf9RlX/hXxfypjnurlXhHXAUusmhvij40sf2ijtqPmA+YfqHnHPoHTwYXJrUYd1zgGpsY7G+8MatTEQt6zaFretEocZiDZ+tfufHfARpbWUL2ZJDHaxGA/h3mL2wTHaWjOKOVBI4/iFbV95LOA6C+e4x7rdMg/vm4QFXrVYyyLaEHbld7im2vLPkTFZJmBlDDIiGuSwqQcVYUIOXWFCbZjZ57yD3D2pZ4HZ9x0gN5Eb9Vp1EeSc0ckfwtT8jzEaI5LQWluJ6UvLgwOTLtEA3wRRpp8zKCRIeY1MdgU7if6RrsNttL2gy3uAJi4ABphle+qvHfAdWs04rIKjN2VB1xPkPOGOwWUS5ayxkqgddp6nGFnTa3p1lTYZgJ6Ff+YbXagJ3QGq0TgARtjgiSYiAIIIIAjPTs25ZZp/QR1Iu/mMUFSBFdrNM+K8uxpm7BplPlQb/v0G+AstW5FyzSlOd28f8Ay7X5ijt80G3v+mUq+at/NDcAFFMgB4AR57o60fGtc19jBiOV5APICAfb97DKF3XaV/24/Q6mvA1X7kQxNT5c+EcmlLL8SQ6Gl5lNK78184BY1G0mFZrOxwbtJ/FTtL1Ar0MNmlLAs+W0ttuR3MMiI8oluysGBIZTUHaCI9O1f0utol1ydaBxx3jgYBJsjT7NNZEa66nFD3HXeK8Osb9I6zTG7KJ8M07W1q7btchDdp3Qq2hRjdmL3G/B4Ql2iX2jKtC3HGTbxsIO2A2avaIdnWa4KqpvCubNspXZXbDjCzZdLTZNFm1mS9jjvqONcxz8Y5tL6yF1KSwVU4Fj3iOFMoBuVgciDyjJGp78jC3qhZXVXdgQr0ug7aV7VOucMcAq6w6HEv8AtUB+Ex7SjOW2wrw/pHZoTTN4iVMPa+R9jjZ/5e84vwcwQCCKMDkQcwYT9NaJEhqipkOaqwzlvuPvHmIBvii1rcNOs6DvqCX4A3aA+B8Y4pNqtSgBZyldjFQWpzIjGz2a6S7MXdu8xzgM7VPCKWPQbzuju0Pq6ZtJtprQ4pLFRhsL7enjujiscgTLXKRsVUFyN9Mq9QIf4DSiKi0VQqqMgAAAOAjziwma1+ak1kLsxNBnjX8mHnWG1CXZ5jVxulRzbAffyhQsEu6ijh98YCbH8RrXZxMmM5vEiuygOUPto7p5Ql6ES/bV3IjE8zh/MIcbUezzpAcEEEEAQQRw6T0mkmi0vzG7iDMnZWmQ+8Bt0jpFbOl4i8xwlptZt9NwjPV7RjIGnTcZ0zFj9IOIX3wGyNWh9DNf/aLQb0091flQbABv+3nFxbbWspGdzRVHjuA3kwFRrfpMSpJQHtzKqOC/MfDDrC/qPZL8yYTkqgdScP8AaYpdK6QafMaY23BR9KjIQ36l2UrILiv9oxPQYD8+MAyXbuOcFy92soFr82XGIatezlwgPONZ7F8OexAor9teveHj9xHBYLc8lw6GhHgRtDbxHoesWjFtEoqoF9cU57RyOXhHmjKQSCKEYEHYdxgPUtC6ZS0LVTRgO0pzHEbxxjdpPRkuet11ruIzB4GPK7NPdGDoxVhkRDxoTW1Xok+iN9Xynn9J8oCst2jZ9mrUfFlfUO8o/UPYiuWQjEPJK3ga3WAI6qY9NBrFHpLVmTNJZQZb/UmGPFcvtAV2jtOo5CTR8N8se638J2cj4xcEQr2/QNpQUZRPTeuDDpn9447Dpt5BuMGZB8j4On8J/Bw5QDpEOisrI4vIwowO7fzjnsNuSat5GrTMZFf4hs+0dPvlxMAppIMma8gmoWjId6nH8/eOiNM60CbaXmLiigIp30pj73iMLffudjOuO+nCA6NFzVS2ozEAMjLU7DicfCGe3adkShVpik/SpvMegy6wgWbRzOb0yoG4nE890WMmxImIQV44/eAzt9se1MCy3JSmqptY72gtM8IpY7PM7o2xoEoPaJEs90teI3hRWnkfGAYNUtGsiNNcUeYa03J8o/PhFjaplTTYI7ZkxVFWYKN5IA84WLZrBIQkBr5rgEFa8jkYC0jCdNVFvOwVd7Gg/wCYqUnWyf8Au5QlKfmfPoD6R2WXVdL1+0O05/1EhRwAriPLhAcZ0pMnkpZULbDMcUVeIBzPPwi30PoNJNXY35rd52z43a5CLWVLCgKAABkAKAchFPpnWKVIqtb8z6Qcv4js+8BZW62JKQu7UUeZ3AbTwjzfT2mmtDfSi9xf5m3tHPpPScye152r9KjuryH5jhgN9isrTHSWubkAcN56Cp6R6rZkEpFQDBQAOmH4hY1O0UVX47DtNgg2hNrdftzhrWm3PjugC/ewygv3cM4Gp8ufCBafNnxgC7dxz2Qpa2aDLVtEsY/3ijh8w/PjDYlfmy474GBr2cuHnAeQQQ3ayatipmyBUZsg2fqUbuEKMBa6L07OkYK15PobEdNq9IcNG62yJlA/9m36u70bZ1pHnUEB7JLmBhVSCDkQQQeojVabIkwUdFYfqAPhujyiyW6ZLNUdk5E06jIxf2TXOcuDqrjfip8Rh5QF/P1Wl1vSWeS+9SSOoJ+xjjtmrNodbrWu8PpKlQed04+EbrNrpIbvq6dAw8sfKLSRp6zNlOT/AMjd/wB1IBZXV+1oAq/CYDcSPuBGLaPto/uFPJl9YdpVoVu66tyYH7RtgEP9jtn/ANf/AFr6wLYLYf7gDmy+sPsEAjroW2tslpzNftWNsvVW0FldrQquvdKqTTkcIb3mqMSwA4kCOOdpmzr3pydGB+0BVy9U5bG9OmTJrfqYgevnFxZNGypXclqvEDHxziptOt9mXulnP6VI82pFPa9d3OEuWq8XJJ8BSAeopdI6x2eVUF7zD5UoTyJyHUwgW3TE+b35jEfSDRfARwQDBpXWqdNqq/2a7lPaPNvSkL8EEARd6t6GM5w7g/DU4/qP0j8xGgdAtaDeIIljM7W4L6x6FZ5KogUAC6KAbt0BmFujDlTKkTdvY5bIFr82XGBq/LlwgArdxzgC3scohQR3suOMDgk4ZcIADXsMtsF+72c4liD3c+GGECkU7WfGAKXcc9nvwhf01qyk6syXRJhqSPlY8dx4xfqCO9lxxxgYGvZy4ecB5ParK8trjqVbj9wdojRHrFuscuct1lDDliORzEKWk9UGXtSWr+hs+jZHrSAVII3WmzOjXXRkO5hTw3xpgCCCCAKRsWe4ydhyYxrggN37XM/xH/zt6wNaXObuebN6xpggA45wQQQBBBBAEEZKpJoASTkBn4Rf6M1UnTKM4uJx7x5Ls6wFAiFiFUEk5ACpPIQ16G1VxD2gckr/ALyPsIZNHaIlSVpKXtbWOLHrsHAR3qRTtZ8YDFUCAUyyAyAHCMrt7te8IhQR3suOOMBBrh3fLjAAa9hlAWu4Z7YlqHu58MIFIGefHHCAA97DKAvdwzgYg93PhhApAwbPjjAF27jnsgC3u1EKCO9lxxxgIJNVygANewy2+/GAtd7PvGJYg93PhhhApAFDn7pjABW7jnsgC3u1EKCO9lxxxgIJNVygNc2Uk0XXUEZ0IB+/OKG3apSGPYLSzwNR4H8GGNiD3c+GGECkAUOfumMAh23U6cmKMjjmVPgcPOKqfoi0J3pL03hSR4rUR6goI72XHHGAg1qO77rhAeQspGYI5iIrHr01FbIA9B+Y0GwSSKNKlluKKfOkB5RBHqSaHkA1aRL/APzT0jMaMlVqsmWBwRB+IDytRXLGOmTo+a/clOeStTxpSPUhKX5FUcgBGwEUoc/dMYDz2TqpaDQsFQH6mx8FrF1Y9TJYAMx2fgvZHjiftDOuHe6VxgINaju/jbhAc1hsMtBdRFTiBieZOJjpL3ezEsQe7nwwgUgCjZ8YAK3cc9kAW92veEQoI72XHHGBgSarl7rAAa9hltgLXez7xiWIPdz4YYQKQBQ5+6YwAVu45wAXsctkQoI72XHGJap7uXDCACl3EQBb2MQoIxbLxgYEmq5eEAK17A4bYC93sxLEHu5+ECkAUbOACLuIx2e/CALe7XvCIUEd7LxxgIJNRl72QAGvYHDbAXu9mJYg93PwgUgCjZwAVu4jHZAFvdr3hEKCO9l44wMCTUZe64QAGvYHDbAWp2feMSxB7ufhApAFDn7pjABF3EYwBb3a94RCine9YGBJqMvdcIADXsDhtgLU7PvGJY17ufhApAFDn7pjABF3EYwBa9r3h/SIUU73rAQSaju+64QADewOFIL1Oz08YljXu9dkAIpQ9787MYAK3cRygC3u1EKCMWy8YCCTVcoADXsDhtgLXez7xiWIPdz8MIFIAoc4AK3cRjsgC3u17wiFBHey8cYGBJqMvdcIADXsDhBW7gMdsSxr3c/CBWAwbPxgMp+XWCR3YIIDXZ8+kE7veEEEBnaMuvrEye74wQQGFnz6RE7veEEEBnaMuvrEyu74wQQGFnz6REzv+EEEBnachziZXd8fzBBAa7PmeUEzveEEEBnachziU7nQ/mCCAxs+ZjFu/wBR+IIIDZPy6wSO74wQQGuzZ9PSCd3vCCCAztGXWJld3xgggNdnzPKCfn0iYID/2Q==")

    def __str__(self) -> str:
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={'pk':self.pk})