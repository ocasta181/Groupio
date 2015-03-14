# group.io
# MIT Big Data Hackathon
# group.io is a group recommendation system
# We are:
# 		Andrin Foster
# 		Benjamin Chen
# 		Catherine Liu
# 		Demetri Sampas 
# 		Prakash Manghwani
# 		Jonathan Barronville
#
# 
# Code is borrowed heaily from http://edc.tversu.ru/elib/inf/0251.pdf



from math import sqrt


# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

group1 = {'Lisa Rose', 'Mick LaSalle', 'Toby'}


yelpDict = {"J-LDiDOvAp5PiE5PZx56Bg":{"L_8K7r6hHc9zAZNBgJ34zg":5,"PBkdlqw53cc2AZsfFD8AEQ":5,"HxolrQy5E06209IOSx69XA":5,"25fxw_jOqZtJwl18cCarIA":3,"2sbdNj3oZEmJ61CmaQcGCQ":5,"2MY2YOCvReXGpXxtN0_a3A":5},
"hy86JlgNqxbSLVMevdiudw":{"G69-uLxHs3h6uvrikivpVA":2,"Xhg93cMdemu5pAMkDoEdtQ":4,"V9euJerhCkh7PXKjtsE2rQ":4,"2e2e7WgqU1BnpxmQL5jbfw":4,"xxq3nX34tsqAtcsSm21rHQ":4,"jcI4ZPF3-hSUPsnoqRHO4w":4},
"zXkYlTLIZTgXH4_wV9L4JA":{"Ca-003BAqWW-IEsFvjlY9g":4,"El6fv45PRpTnI4OnAqQHdA":5,"emQkvcck-uqUanJafLIKOA":5,"a9-qixaIQftb4HNZz4ocIw":4,"bUmnZJ1DjtDP2_qb2M62mg":4,"YbzUYOY_ZIYTWGNw8sbgHw":2,"Nui7Cnhrhrm4Ar2rcSHbIA":4,"YRDKsBFYP7G0E8BLJKIkvA":4,"jgc_K9MEC-a_oXdy1frvKg":5},
"HeIv2xpid8OSu_YqFs8inw":{"8v2OAitccSfmLOrjjxr1YA":5,"1V1lodaiyYw4ZKyiv95pyw":4,"nH4CEJwrRXPxhfdL2pz3MA":4,"xWnS17JRqB2Cjdgfncnnng":5,"96Op48a-5MMk9sTOd_V7NA":5,"vM00Chr2WiS0lKtOudEVag":4,"CqKiF2X0_4erH02-CUiweQ":4,"zmvIqh26-lzpZROHuhA-6w":4,"3f9oR4imL5js4nMPvNIauQ":4,"T_FMm8BNUIfUOhE-ScV15w":3,"4c7xJ23IV9VFWhHjdWN1aw":4,"aYGh5LBKzajGS5JjTkZRhA":1,"LA37y058rLD9CnIdWMyPpA":2,"y1Q3nJR20VMmE51sK5djGQ":5,"HjM7hG2Fqrn6ZGmffs5aDQ":5},"g7d_6seo9-B7e53jw0rAeg":{"mU57qypB4nLScxgowHNEUA":3,"JGeWyuOFdutslFBM3GxUcQ":5,"Lq6CDJ2yHmMs4N7jscQhHQ":3,"zAv8Tn8ljL6iPAkoYeRnlw":3,"NrmjX7lp8LfqdJSd83P9-Q":5,"KuQVzAzJZggFLi60OlBhmA":5,"8hnjKa0-bQtvbESv51LoFQ":2,"gRGR8p5pCFT9Pho4VXcMDg":5,"HnhDu5WPH35KBjBn2PNwbg":4},"YKgBgDZZx9sPa_eie6LUnQ":{"eWPFXL1Bmu1ImtIa2Rqliw":4,"tFU2Js_nbIZOrnKfYJYBBg":5,"-5RN56jH78MV2oquLV_G8g":2,"8Mb6nc1Qt0cXWue67DJ1aw":5,"_CHH9KN1bO5cs_GHjQ-r1A":3,"KjymOs12Mpy0Kd54b7T9MA":4,"ppoP2E7YOZpa2TmarTY2rQ":1},"ChN9DVAAoNHUY6JljBcPqg":{"Q_Rwcv9APBLggk2KAsBEvg":3,"3w5gd4EuSc75UKYMJiNUPA":5,"M_b7P2IBKY6zyqDmXE1kJA":5,"zabyU7o0GUbKx2TcGDiptg":5,"BW1JCE3Qj4uIokg7kLUL7w":4},"DxGyd3qtW4BcJjPimDN_NQ":{"uyEUL3Oskfa1fOYCksyM8A":1,"CUrGpz9_Tt0ZaOKCCjwP8A":5,"z3hkiTwFgHx6P8IGUABfuw":4,"T9V8pY5aLMM85cu9xVP3CQ":4,"G946CmZ2NtOeOSftF8tbxg":5},"f-35UJra5K35PUU0IiRyaw":{"6bBJymP2jh-tenBY8zvL1A":5,"dcGya8UVCL8eqfPqixMvYQ":5,"kCNp6j05zCixFt8ESfkRpg":5,"ArhWxXLmPiyShXwBQvoUUw":5,"sH4ayCIBNrPnmAJNQZ3xIw":5,"7zyyc0eWB258D9YW8DjVYg":5},"LT3L8-tthzD0IakgXm81pw":{"6JE0fp84Ws59Oh_sQoaWkQ":4,"XHr5mXFgobOHoxbPJxmYdg":4,"i2ZfdVYWL9GnOD2gjFaMlA":5,"H6F8CVOFILdnSUQtmvy_zQ":4,"NDKkce5Au-o_OhIt5f2ZBg":3,"sZAzeccYUVPjlkrlMooV-g":4,"jbKVbSz51F8IcewsiRQu4A":3,"-_npP9XdyzILAjtFfX8UAQ":4,"r3r_bAfa6pZKIhQB82FizQ":2,"MLVKDbuI2xaOJQ4-NZj2MQ":5,"VlG9qxAc4d0em2djaU__xw":1,"St3jS0PnF1lulH1ggA4Jgw":4,"XNSito__Fne14TXU0vz1Qw":4,"cUaaIk_3UdeSJ54CLvrW8A":4,"Bui7TEFaPwuZtW5QQg2oFQ":3,"c0RSs2KYK5Y-ZlSrNq9LyA":2,"e9nN4XxjdHj4qtKCOPq_vg":4,"PxeX1M8WtyPxX1MuuGIh-g":4,"UIGFrEcoDsw05I1UOrxdOA":4,"d3MxUXS1b6U2P_gGuCO1-A":4,"F3SEkW6v2LJ5y6Ldo5pPaw":4,"K28O8R76bJFUt57ScN46Mw":2,"3l72FflaaeI0tWEAWN3-gQ":3,"oHjoahzL5F0m-OGDQouEGw":4,"PEOP7kZ1E4BJx3YzLMrmpA":4,"B8ujMtvvpHyEQ2r_QlAT2w":3,"rIpOpzVNEBNZrRFu4n_JvQ":2,"qlrZzAktK8wODSHxhLEK7w":1,"3n9mSKySEv3G03YjcU-YOQ":4,"CFaRVxsnN4Zjf28cbORKIA":4,"x7M9x4AqyC-oYk0rajrOWw":1,"SPBZxmt8_nT30rNVnKHYKA":2,"7LGjM8HKJTwqfYU3C7N_0w":2,"pjtB4FadDdq_DeyedjDsOw":1,"h6jfMpTZpNduLG0wE2tbaw":5,"0qUesn1TBPpPjW20h5Lqfg":5},"8Uq8gSxmvm6g5VBlEuSEUQ":{"mPDE4dMqAyLZNCR-tEYQ5w":2,"jOuERtVf7QePnK9ZcdH5XA":5,"aGbjLWzcrnEx2ZmMCFm3EA":4,"BQjGE1Z3nk253XzIZqt8Gg":5,"DqY2VlbRuQ3Mu2mlxd4xUQ":3,"34uJtlPnKicSaX1V8_tu1A":4,"sIyHTizqAiGu12XMLX3N3g":4,"WIlklz81DcJkUWJThbnJbQ":5,"QbmcCE_cLq4WO8ZMKImaLw":2,"bCRrLdBLel3y73tA8w6C3Q":3,"zt1TpTuJ6y9n551sw9TaEg":4},"i3XJGwwNO_ts98VAJe5C5A":{"jOuERtVf7QePnK9ZcdH5XA":4,"_45p8kOA__aNycVVe-n-KA":4,"Xhg93cMdemu5pAMkDoEdtQ":3,"nZgYNbl1XlZyyKlISMoG6w":2,"sxRI0je6hAR-MeBDxdyhug":1,"uCoNIQty4nPrhn_WHo110A":5},"6dSkC2oJ825KBknfuSkPig":{"Vem91uL0NUK_HzS4qNdJAA":5,"-R7hAYD7oCuEfcZ85u2Zrg":1,"EwjDhE_19ELnkgVNAERUhg":4,"qn-hjNuiLJll4zTG6TEBZQ":4,"H_cEQY47mK5LDmWW6nX6Eg":1,"hr41l2QX7OHh3k_x0Zk2Vw":4,"Ow8Y3uwb9zlIhpfXnz7K6Q":5,"C4CbD-0Rz4nglavf_0dRdg":4,"ZmzjoG4-9Ix50l4mNgB9xg":4},"uOzAOdk_7v9eX9w_48oh7g":{"s0q3j_-lW-rZRdgept6wZQ":4,"3iSDyQHZHuoCFn-GlM5lsQ":1,"U0LtcorP6rR5hGxwfV00HA":2,"O38pLbYGB02DtL-0NPSwsw":2,"LtHDWK11yb-XZg6KJjxO1Q":4},"V8PvONsyzCCGKJXBw9KvMw":{"gGfK9Qq9gSQf_4gr5aS4IA":4,"EMOFQciQnAtCjZnMs0z4Jw":5,"hHAlLNh4q7n6E5PTrtJZ8Q":5,"e8FMAuTswDueAlLsNyLhcA":4,"7_SWD2uS3yVsFXzuw8k5MA":4,"eUbpbGBSe0oQneuAenPasw":4,"o-DRmVihuTjS3x9OXSj0tw":4,"Ane4XcpP7aWzhjd8SGiciQ":5},"E2oFMuZK4-0hZzAMi0PdRg":{"RZTcKugP9dGWFkO4RpbVEQ":4,"jfDBaBgwINrGYAo8p2MJ4g":4,"HtoKT4TVWr479Jdk2E2lXg":5,"hwXFp8FKJ7ivQb8_f4X23g":5,"RFeDe3fNr14kvUKlVx6_4w":4,"VCE5ulTtn-lt6nYfAiPnFg":4,"o1GIYYZJjM6nM03fQs_uEQ":4,"9Y3aQAVITkEJYe5vLZr13w":4,"cInzGnaFZ3EIItvFXl1MvQ":2,"_PINIylE-HAtznOkeQ6OOw":4,"mhQCxOiqp03qnhGRTtPduw":3},"UFvCKo6vi5yudcJGF9uEug":{"sj0WHhcby98NXWCRxXkqLg":1,"_20WCD89imWx15jlxv7kGg":1,"BINYfrtGp3A4w0d5E7kbYw":1,"uDINKrN9OyKqm_pBz8OCHg":5,"EC9WB-iVjd28B6R6KIZ8TA":4,"aOR_hD-xXsnU6bgVcJ3uXw":1,"itD_VnpNJnfua6dCPp7EFA":2,"f9eFteZuBoZqzYg5UUrufw":1,"bgTB6MgdVQssXhkNJ7qIfw":2,"uKSX1n1RoAzGq4bV8GPHVg":4,"z4KFTJQsAdxqMZA7Fx0A9A":2,"vuaiUkJ76tiN8B2s1aFLdQ":5,"un3KC2gyMrSG6yqjVRctXg":4,"4zfrcEmGvZ4oYKx_revTxA":5,"eXaVJc5GMIjYEUjbrc13FA":1,"lRpke2ux5ywaiQ8phFA4Lg":5},"k-gGGTHk6Lqurs0Wycw6Hw":{"jdtc9AARnZLOi38Qvkdm7Q":3,"qWYdBWci87q7JRZenrGzYg":5,"zj0BkAi54BGU_AK6AyvJDQ":5,"KkRK8hZWOBj1ZZkC00cMhg":5,"nEf8wej39m0EsVP64LZsOA":1,"9f5WxUG_Vc-PzBmX6SeTew":1,"YyxR8Cxbz54-EewVyoyNaQ":4,"Km4kapPAmTIjRlrjjfI1Mg":4},"0dpNmJxKp4Ha-fzJ2R8cCw":{"LzNJLEIo4gh-X_rmDkNkNg":5,"Vtx0VYkybAd71fzwgaoQ8g":4,"eJpr6Ks8pr4bmvDVPTN-Xg":4,"80peW-kivTjBBAITGTcqDQ":5,"h762dZ33uhSKtLZ-21u6Jg":4,"wPriPtODfiaTatTIKkOSqw":3,"N8qHoaCHdg8ALiA3WxEHkQ":5,"L_MtTn4IUBTmQtqqM2iFqA":4,"2e1jzfiHFGCRpV66gYNVbA":5,"oqQvCiG9FDbIdr6M4yen5A":4,"nNyRP4T2wR5xPaTdQoYQVA":5,"WSHQ9qpL39g5xA3E5iBCmw":4,"73F8ja26mmWnKhiJQVXNmw":4,"D9EW-5pB-FvG06IfMJZquA":2,"qZXZvY6Y2QreIYcS9uv65g":5,"qyqOfpsAC5ooVROm7fB0jQ":4},"i_WyPpbIszujIB8eCIW-Lw":{"3Ms_jV2Pp2VFfz8CqZcDjw":3,"Zqs_uU5GA-VYJlv0zU-MOw":4,"I_ObbXRqklQmV_L_QLUKjQ":4,"kzB4VVSQ-sXsQXkvDz4Zfw":4,"OAfOKYY1SjDfjrAFiqPNLw":4,"8-gMpvexcH1mrApghRiAhA":2,"95RAoc1wnt2rs28Wfs6_1Q":2,"QbS8kEuBXfN6FN_JCuFLuw":3,"TkwbYc_lS-wpaVqMykCxLQ":1},"RNoMJJwCVz8AAR-usCvYUg":{"cRwNwAGQ8Pc_-orLefrwRw":3,"TP4ibW_dRx-jIJM_Ytz22w":2,"1_43FZHx3P5D7X-CpIR9WA":5,"CqhsIZ7TzCfJTrZqg5-gqQ":4,"pDXv67UQjBKScEgGhc5yLg":2,"PR5KXD_CUs05MGfXJ8CS3Q":3,"05tazaFQt1EnQ_Gk_1AFyg":4,"lddbHJKgFvnVWabK-M8TPA":1,"9f4cTpQh7E4HB1Tl8Hk72w":1,"rKbYn0Nssuc4S_9nq0gcHA":5,"pF7uRzygyZsltbmVpjIyvw":4,"MTUN0lKKoq7yN4fWagJ-3Q":5,"Dp1VAj7SIb82CuwVDLah0Q":2,"6Q_WeP3JxYoFciwcjMStWw":2,"R1kKjAO5kZO6d0gQGqrvGA":2,"5qElnvC0danGy0io0-NRKw":5,"aozcOaCMwOHG8s-lbZ6_gA":2,"9Ep4sguv3HH_8lWyzSogjw":5,"Qr232ykh-d73aAKQqfdu8Q":2,"5paMI5Hhciyl09yGpzdoJw":5,"eHcQzL5eebqvKrLW5q283w":3,"Nq7eB1wB2EArUICtiNePvQ":4,"GkxEw4VTC2eGUYQMf02pYQ":1,"rNqvFXxGSj37MsUI6GyqFA":5,"v7OwbHgNgy_VQ9eP5FjvUA":5,"MPHoF6kRNZhxcDfxHeoUlw":3,"K7B9-RFdQ2nMNws7Ph05Zg":1,"n7sXYcQRoU9zs5DAekFmNw":1,"TisnIBR2lMvT1DMC95_eHg":3,"W010P4plDADjo2SFq3OvXA":3,"byFWmwlVSmUj-AmM6NZYvw":5,"OGBBv1G_3hyqjNZdUfPLaA":5,"w8y1dQ06MckD8_fJvP5jag":4,"1yx2zLskVTe5WQdYjL2Apw":2,"EqyNGesG22jNfNT5pmfYgw":5,"l0QCZhMOPUId1Xfp23yLgA":5,"dp0unqYxrYzvfaMVVmk6mw":5,"863nEWkPZ7uD-ZRTmmJokw":2,"FucrEEO2laIlAnIZ_n6cTA":1,"0EBR4wDqtkbMC-wghpctEg":2,"er1Ng8wxlwaWnzFAKttukQ":4,"3E_toMWSUCuhRJzG1eml8Q":5,"fowXs9zAM0TQhSfSkPeVuw":2},"3q8by393Q40Xc3wTIIczAg":{"33aOj9haiHsULCUmFOZ7uQ":5,"Ni9aqkG_fNWrH02VNlRhLQ":4,"TUxCIJ6Jj2lEOqoVIoUH4g":4,"Cu6LurwRHzjK3OGmvK18pQ":4,"xfwRO04KbAPw_zRotCfWQQ":4,"1yx2zLskVTe5WQdYjL2Apw":5,"olwuTiAEEFgSYefWUcZWbQ":5,"3dQqoz-yHhOfHrIBMRCD3w":4,"4tOxPT_PpHq2LtZAulyAJw":5,"pxi-I0OBnZOUZSS2ZVwrRQ":5,"C3WAtjq006LVC-EHCt-fRA":3,"zVm_q6MF82j2rlc4p5d9Ng":5,"Zq-yfLJYy7245p-O8-PqGA":5,"6FMkGfbgUd1MGLvgSmT_Bw":5},"N6VcdNl2x461HTwaDe6EHg":{"3w5gd4EuSc75UKYMJiNUPA":5,"eRRyfI6QVvSviirRF8UGzQ":4,"4bEjOyTaDG24SY5TxsaUNQ":4,"WS1XuIez_2KP-3RJD-r9kg":3,"OiCxoAIoBvEWxf7p1qVVmA":5,"BAFb16CUpRBKjG0a9189GQ":3,"Es300Ys1XXPYg8aI7BKVYQ":5,"TWD8c5-P7w9v-2KX_GSNZQ":4,"JpHE7yhMS5ehA9e8WG_ETg":5,"LTMEAdWM4m5tIDCSrkALIg":4,"6LM_Klmp3hOP0JmsMCKRqQ":3,"eq6lQI039SBLC6sHm3idGA":4,"N50HceZf1595UtU867u4uQ":4,"1U1GRksKXF7q8FKcW0e5VQ":5,"QW5z1BpyU4S7vHF2LJNNsg":4,"Pz7SWZQhxL6ZbhL9jE2NTA":4,"k-D2NUfaUbuQzPaMXniXcA":2},"uufF6Qu7NjadtQezp0Hqrw":{"SsTxjxo8qvqBMvan1rzNzg":4,"DO3Gk17RyJVW7zYMCtYPnw":5,"UpMR63WZgIn8VDKnYpDwXA":3,"JS9Bao1vDxM2BGWMYjEavA":2,"32f43CI5i1oCleGZG5kQFA":2},"YHWjTb22lMcSTxr5Od_3sQ":{"GELMS90-RDnSuLEFPxnt3w":5,"eq6lQI039SBLC6sHm3idGA":4,"sDXINrHrs8phlkzkwQNiBQ":4,"bYhpy9u8fKkGhYHtvYXazQ":2,"Es300Ys1XXPYg8aI7BKVYQ":2,"2e2e7WgqU1BnpxmQL5jbfw":3},"HoXgCssSqjCExxAG0xf4_A":{"_-VPCIdtP19HQI7CcsfVTA":5,"7O1WVPggPtAbUdQsT5id_g":1,"_3R0ELm45KHRb52rAilyOw":3,"TuuENwzxOFdDLY_oKCbFZw":3,"NYIyTj2AZJpAo7XIM-Z7lw":5,"Lnohr9bpCbHNsomazXDg-w":1,"pJ7U2sG9kPauu2FLWKX4QQ":1,"x54XQbvx-rfW4KmEMERztg":5,"TMZP6Kzkc-FytzgbgIC9JA":3},"lMZD3OpQOb1VijGm2sbfbQ":{"63rmr1oM0BbAXcUfNEaieQ":2,"OIPE8yU_DRt6ZN59CcMBFA":3,"sbAkrBIVXuQG1U8e2wyhqQ":1,"04ogq23JnzauhezrWEXG_g":5,"Ln34kwDUNZPLhVhUqauLWQ":1},"71Gnwsn6XGae6n1PEu72ng":{"Q76FbDBBw4Mm3RZ34cpZfg":5,"ROQQk4mCm4_tebvTEGjhEQ":4,"d3-h8QpXoQnUlC9nt55HTw":4,"C0a4YXdOTlaVIa9mzT7VEQ":4,"Z6DfLcBqRwFv86u-ddVYDQ":2,"4CPrhBc4Ado90fj7PG6jrA":1,"Qis-foTefAEG4Ut7UIEWKA":4,"-4lREdSYSoRGs9sQcfJTRA":5,"L9AlMDqwlKpVDFTcSIw4hA":4,"LxCf3sDhSiOWH_xJTQfFkg":1,"Okg-KUAwf3qJ4kkqkAn6oQ":4,"watqY4fLMJTqs5UgItegGg":5,"D412fP4iqVVQqo6JsSSZiw":4,"cwXL-MVpeSBpZaQ_uqaLvw":3,"eNIDbboNe7W_rAnNHoveEA":5,"YbqNbrnOEk2T0qIBbTivuQ":4,"41uh9gpSwCfiJuK3EaHisQ":5,"5xk2-s_QsnHZxycl5yQ4Gg":3,"4PLnC7qzszbl_MQVaYgpJQ":4,"7_4OqT_IQbpXlao-4BEyMQ":1,"xmA5ZYJPzt0-Gyim2rynjA":5,"UFvogJEUiLSJwyx2LSz2uQ":2,"IZiK5hhmLGq3kTKnCIfzUQ":4,"e8kqqWU9247Nn5VAF5sDkQ":2,"ZA_F3NS4C7UGQubU_lERdA":1,"yT3OITYWbjqKM15mGNXmyw":3,"egGk5zPJIfgIwlDPjuaVaQ":4,"B6GFHIchPAnBLIHGD_YbPw":3,"0L-d_BgUto2XJnuncUEpnQ":3,"FRYCe6Yc0rPzzloSWSsl1g":2,"1olAT5l8ZiKLVavyWkeElw":3,"_mrGYF6uScU24LcwshEqCA":5,"ioXu3MhPt_v8f5wTWJX4ag":4,"RGmR2iBzqI3LEMDE6J8nJA":5,"Uq9HDxWQLV3O0K6Rrlk64Q":5,"STcLx0y_X89TsC0m2gVgHw":5,"-LHHCgIUZy49sUU4j03T2w":5,"etlJh7qmqK1mNgAcmLUKrg":4,"W33EBdIVWmr01_vBk1JjVA":3,"L78JwNkiYSuBfP8U1zTB-A":4,"xJX0u3s9AJOUBDpXkt1zMQ":1,"GjsA7N1j81TjBt7hT5H4YA":3,"WUtPI9rJbs7ET1gPhULnDw":3},"BGzYj1GQ1gwIhd5cYIfU8A":{"eGj1NnvbIUVWgDYQWEOwQg":4,"W-9YqWhkfeK-K3xGFvFeuw":1,"DDnmNTvIIQu2t3WZ2EQx-w":4,"trAvQPp7gps0Btk-2AmLpw":2,"jtzhY-P4H6WSYpv5rWhxtw":5,"VlG9qxAc4d0em2djaU__xw":4,"jLXzOraBKPBIavTMrVRhAQ":4,"G_2CWsU7GYwhNqptrLXUBg":5,"bzDs0u8I-z231QVdIQWkrA":5,"JTuTbztTMwJ4rpbO9Q-hCQ":5,"ybXlbfOjrKDdz5NoC-G9Gw":5,"n-XTO7I2o2h06o-vyjtYfg":5,"iXT19WQLq_5ua6uFNuVKpQ":5,"FFCkoA_L3cqYXtHtLyvxwA":5,"HIiVx2mseVWKtx8TKfWC_A":4},"OzbDvzLS7FP42GV4QPTUGA":{"SkcccvAydbt5zlQI0EUL2g":5,"_oQN89kF_d97-cWW0iO8_g":5,"VY_tvNUCCXGXQeSvJl757Q":3,"jDZS6BUrz5PI-M4iQCTMsg":5,"mkLVdKIReJQicOT8a4O7YQ":3,"ask-mVRByAVOrHAgGxySoA":5},"s10b9Ozb5RPKrou6T0v57A":{"rHtkiJVIT-AFexNcEQ1vYQ":5,"zTfBa__ldlTdbVgSl5h31Q":4,"8ktREOIxt3kRdJpJK7jpfA":5,"Ug0LxMh0mZ0j0A-QjKzWng":5,"j5HLcBru7FEirYJPbKFVWA":5,"w43fQnuFAJVX9AsS06vwXA":1,"irVjrnurmB03bTaj9BXofg":5,"lp-J_cO5owuMzGJqdn3PNg":4,"6OFYUDvf2k4RXDfOomfi1A":5,"uMxfxbqT27XDeU9UTXeErg":5},"5eOjREaDIXXiOOdjuFSEhw":{"_9JDgUdXbCn1Vx-nj49VJg":5,"JokKtdXU7zXHcr20Lrk29A":5,"NYIyTj2AZJpAo7XIM-Z7lw":1,"7cfh_iFrzh2489palOKKmQ":2,"8SgxmzOgLUCnkuVMs2NOrQ":1,"qyHsF61vhG1PsWi8PoNAYQ":5,"-DgcMdW6wc3UAu2c0tJFfg":1,"KHdadnkfYm0OgyIF_fvL8g":1,"cmI7xMaYAOCce5K7MvsWXg":2,"M0Ulu3PzwBumgOZJL-6KnQ":1,"KBKDl08flVw1AqvM5ucVpA":4,"bAWpyAuXMNnRF9_UhtBOmw":4,"hyff2JyqQgf85MaJZslHCg":5,"GNC2WXRjEO8e7r5f8ZCVrA":3,"wdkVP5rNQHCbQTSBVfJrgQ":2},"GmV6ndNRG3-ogl-odjD1-A":{"PN9w-QGQtSwCmf4jcrme_g":4,"nt5HVhwaL9VqsnX9-6QBwg":4,"uVnMnzOUrMmh9bbqkLeauw":2,"uR96BDuI8YR7gqbc-Ncg9A":4,"-cOzkNEQIdF1g_4o4M-uGw":1,"LLDGTT7FExklkQvHebEjRg":5,"34JQEZg9DgTpzZ8tnAw_CQ":1,"aaNEAZUn__VG6vl-YDC_sg":5,"83DsSlg-swjLzmZnUzq2UA":2,"ESlu79Th0bWSPqtPh5rWHA":4,"p_RGxnaMCJ6bTL6voUymsg":5,"3mrp7wim9_rCMTO3kRp3Rw":4,"JUATTlFUONx_er9_YRFDrw":3,"K8dQr_82-DMpDudEv8PDmw":4,"IiVJ2_OdjWzEXZ7IR5r3Hw":4},"ssKxICaHvUSQ1Va-jSK59g":{"jEf18KTlek4zRHdsv6kIPQ":5,"rXEGCpdboVwczMIDZuXXaA":5,"WXl4rymMskrrNlK5g6ml6w":2,"cmv6wUUe-H0xRiFEY0__iQ":5,"iChdAsAIPgKIhV7fLOkt1Q":5,"6xxlx1m1rm2jYvsWcERhSA":3,"eG3Kxpv-JOLib9o5W9Aiyw":4},"VUGUyClHO8t61EUll4feRQ":{"yOlDmC-AcBQwArkxiegG6A":4,"iDYzGVIF1TDWdjHNgNjCVw":5,"UVEnZjATEGkKLFdzV_dTvA":5,"RBvQPI6xn2GmiAOnhirBUw":5,"GfsKIdURweoz-V_X0XwoPA":5,"i6xkstDGPFim3inpO71_7g":3,"VSPuvNSDUvlTl670lVAkkw":5,"33dsgLr8_SN_mhRPEamu7A":5},"miIyE1hAi2je1-V8it2X-Q":{"n_ZuPiXgB4YPbkuSINpabQ":4,"rd3PEVYGnW3BOzC4z5oLKQ":5,"yPibH0T8M3EbM550S9LSHQ":5,"n5eQnMnVVt3FfrFENYoU0g":3,"UCzaZ2z6E-Xy8Vn-MLpIrw":5,"1x6MlFYhRSzbGZ_E7kICvQ":1},"2A4ohnClHl9aPjBQBYXlbA":{"tdDp5kMt8mkTz2xAXaJK4A":4,"bp8T6-NZFKw3-Ga6ssU28w":4,"3EDCh1Wssaak6D7OXx1bqA":4,"Kf1e8oHpEeqmsAMAtN_p_A":4,"BwKoN2_RppV8reMC5KmP4w":4,"BvacFV7Wr_dUlz3M5-aJ5w":4,"BLTrjqOHhtg6yYk8ObeAxQ":5},"fH210XPZrnw5YSqeHaushg":{"jgbEZzERVI4yvAAtXWW93A":5,"DdVbzqR0z3NisbPupv4IJw":5,"U0Up9AYSClGwmuqo-ZJVzw":5,"wCi6nBXnXf5PAHqJZP9dqA":1,"OEQMqI-duBA1gbBFzi7BPw":2,"DPVk5PTQPYuVA5t9wOvGLw":4,"IRUsIQSgjkk7Ah5RBsIfJg":3,"rrWhi2TL0smrbihvavZxcg":4,"z2YTaHtGod3i3BBbKiMNwQ":5},"KKMyI2zaTYSOD3hda6KvPA":{"d-S7YIbeKqUAuspIoOedmQ":2,"JFoEf0Kn5GgFIKvAB7DQ3A":2,"PsOvURXqpy8iZX2J8y429A":2,"Bj3v6XY-0arzKQmT0giSKA":2,"ieYiud3trM-9e7E8YUhK0g":2,"SqpICnZPgxUraMDNqu-YwA":2},"4zeG5Q7rfGFnpXsUDDYqNg":{"k1U_xkEEyky4Fq7rNijzGg":5,"fDZzCjlxaA4OOmnFO-i0vw":3,"8cL7aJVKTYmLguzXEAS3Lw":4,"KDQqjVfqmLDwddpt3yKVNQ":5,"I941jBn1KURuN-2wygJ_5A":2},"ZDpjrKSblBHSH-Mpo67-Vw":{"Tk4BA8X5kkXxAFTs9piHMA":5,"oR8R39yGJQTRYEPAoJagrg":4,"P9pZLGjYc1j7VPO-KIBpMw":3,"rzR42pfVlTP21XsUgytPJQ":5,"ovyETl0O_ndbNQCj1maXMQ":5,"eMyeRHm4XCGgGBcb9-qcEg":5,"O5rT7T6nW-5mUHKeoi68qg":4,"ExaVbfbM2en7MCCI1_qYnw":4,"wCBpyIrn3RfJfS0CZjOQrw":4,"yTDNPDu7ZPRO7vV7vc6-Dw":5,"gWZt5lnRQPbTwXRi9Ik6Tw":5},"q6DduWRtbDOZwsJSM3A_5A":{"QSKwZM0K_0CaFs65tkksjg":5,"KjEFFEEd_r3XqGaWpmsWpg":5,"D90zYKXq1HcOiWfBgcaWtw":4,"mRu8SmOrVJObZgm_dfkVjA":4,"2KLK0wb0gRJEdJwBbv2lvg":3,"mPoG-nf5jjOE2H0A2JSX7w":5,"eh4LGMrkNQl8MSbrfiSCvg":4,"1_hLQFlNOOjNy-5WVyJwdQ":5,"rVnY7LkVgtVyXcyQ7Dzx2Q":5,"hdoCRGSy8V1wPjwHDS6iEQ":4,"rvJPjjWq5yEi7RNhgC1Q6w":4,"Gyu9Xu7-I5NVNDTgTUnuMA":5,"2X_IKaaeVgm1v9SBNeQxkQ":4,"Gj3eDIunoz2jCGKFicyvCw":3,"Z6QAeL9nUlwKvps_MYf3rg":4},"HwuAC0BGIZcC3c-vkVQpgg":{"fikT0uXLoFBy5FJGHBvtTg":3,"3AlN2XZ0I0F8650y2yjLWA":4,"TW44bipmQ5fCYbA2D2sajw":2,"HD70O15LQOIohX0MoIt8RQ":3,"rQ87T7pvTJ4H7K-vYYTQfA":5,"u7-9OD_9qc6PDYlMk0-VcA":5,"aGbjLWzcrnEx2ZmMCFm3EA":5,"3W3e6nbSxePT4ctJGkljZQ":1,"qt1L3A6TpSw_36uFsugUew":1,"8_HGHlHsNdCnTsLQYHteAw":5,"Te4VWxW8ceXp86D2fG5SOg":3,"JVHSFeayUur0ksdhaJvvMw":3,"41zxbLn6HZQfME3uWbyM4A":5,"se69XzY9Lhk_Qy5QFxTqjw":4,"Fh6OndE60vzvyhCX1Wg7Aw":5},"3WZK3Zpbmoe1rPkX2_woqw":{"aSZzH68--YxNQYAO5nKBkA":5,"BYQz12ztqIC54cmAEdCYDg":4,"-KDCNt72VIuhV1rSUlF-eg":2,"kV768Ru9q3JKNNaKuKAKCw":5,"9CLZ-Uwv3nmOlbbGCIhvrQ":3},"E1bI83_AbOLgehzf1XOuhA":{"fSs0EdKmLJ7VULejtsi9CQ":5,"lTvW5TcIVIVNmE4_LYQ4eA":5,"AeKTQBtPRDHLAFL9bzbUnA":3,"Q3a7xKU_KrOT8Mli5X6aWg":4,"k0EfcQdHrgGuW-4DVR8XVQ":2,"OHsuvX4rmhnPvvRBb-QK7A":5,"UEyXv6C3CyxVYmxRDWYgUQ":5,"8871Si56d_dc0igE3TRpgA":2,"3JTVc83KpA37yhrkwHzlvQ":3,"aj2FShIkWIm1i1qnTljP6w":5,"qfPJgYNaJ-whCrjVgFCsyw":5,"27ADmOieSUZfbiU15als7w":5,"Bm0KsXgbVl48sJPhb5Exdw":5,"t6SuvEq9PPVGzNv5bJzDtw":5,"YHoYNkc9SdrQbB5lgc9FQQ":5,"jSDLdzm7ZbMWL3g3D2GU9w":5,"QRXv7Jvq_SuiiT_SKvbdig":5,"uXu7hX_bTrr-48op0Ykkyw":5,"lAher1puKzN9r3LALx-JqQ":5,"orRee-skZXdMw0DYtMGo5w":1,"6zfnccQkYqDFYNZHYoHo5Q":5,"o5Xu5zGBgL4jruUXudm2yQ":4,"JmUf7RUDjFc7PhCAMSHSuw":4,"40VsC3U_JLufzJ6b5GhXTg":4,"awchAzxp8VwNcgj5oz9WDg":4,"Nqcl3hDLyiwNQBxQpKCdIQ":4,"3OB5gQqibKGTzx9R1w7wKQ":5,"5yunjzpxeK64bot8LxWTuw":4,"mpXeChWrq1bcRWAEgufY9w":3,"v8TQwyxEj4or2Yng6y0S7A":4,"8q957qOv1wED08Rgs0-VGg":5},"CSTWYMmUfbZCM1AJP5Mc-w":{"jOuERtVf7QePnK9ZcdH5XA":4,"KcSJUq1kwO8awZRMS6Q49g":2,"zPr5YhMh17IDvaVHgvvs_w":2,"4bEjOyTaDG24SY5TxsaUNQ":4,"MuIXnv7Oq7X3-4aEsp9dDA":5,"zuqsWG_FamUP3FQnL49Q4Q":4,"rfDTJLEwZZ2EGOZiTDdqQA":5,"AtjsjFzalWqJ7S9DUFQ4bw":5,"GhQQsSApIRfUmIcqzmSaGA":1,"5ambRqdTJt9vGwFzVI9HBw":4,"eI28wIzw6ZclI9jGXhtbow":5,"jf67Z1pnwElRSXllpQHiJg":3,"W4A_cYOAHhOQ-wb8E7suvg":4,"wV_LfsaGrxv4S6eiW9N8Eg":4,"Ht8mXLuqJSTPrU9kvzosUA":3,"FzeYyIca3Bw8mS4MeUUAGw":4},"TQlcm6sa-LaIlf8o0LaKaA":{"qbEJeRvytnBo5BGG1R5kGg":4,"XHzZgNmJFVHeT3unDg2Qig":1,"t7492xEXVTDGvuihdcaC1g":2,"qT4w8n27RBQ_slz_FiK0CQ":5,"QQ0VZ1ggQO1aVf_GK6kn5g":5,"RlfX4muX5LfJsvmI9qWGvw":4},"r1kPqZaXmJLsx9YbdJdCUQ":{"0K634ehk41ZRc4kj3NTAEQ":5,"k_aOcqWOHWprjs7ykdzlAQ":3,"Fo424KetiOnQp0DVJooYMw":3,"MthnswWexrUtCzH3vS5YnQ":5,"kUvJiI7teJ--m5i1ReG58w":5,"LMG0zsAkUSscIvmV9vvm3A":4,"cwAd2nytPLKmABtLXsgpIw":5,"AZAd_Zhv4UiJZ1x2FRPqIA":3},"lS-vfIkNm0YH6ksbDqeWuA":{"A3Jv-FFRsDEWXxKJ6ZIxfg":3,"88CNSyeoKhGn1x0SHvz8Ig":4,"V9euJerhCkh7PXKjtsE2rQ":4,"bCRrLdBLel3y73tA8w6C3Q":4,"kV768Ru9q3JKNNaKuKAKCw":3,"BW1JCE3Qj4uIokg7kLUL7w":4,"tcphcsPONrP82kUyvcELoA":3,"vcLHeYauRsqqlAUzNVvBig":3,"2oRj5Qh18pCMPlvHFmyoow":3},"qVuM0V8k4eQzNujswbxehw":{"YK9JsdBPgMvVSIGMuplX6g":5,"X4G7Zr-7fOr1bBP4iiONuw":1,"cTz7lxA0AdWKMba6Bvsi3g":1,"0H7ewZ656xM0bulSMowWtQ":1,"G2AqHSVc8t6I21qiHeq7jA":1,"Hieqsu3u1peZ2I2jPwiKHw":5,"9xGeYICHI3UoTcvlIKwWzA":1},"SimBqxBHYwkPE8X7f_RnVg":{"_-VPCIdtP19HQI7CcsfVTA":4,"gtai_-E-WUGr_8tYYik59A":1,"8Gmjirpg6V_a2u0K4In6Iw":3,"bRk44ShCT0osos-1xaTRyA":5,"AjHhlZJ7FSp7l6f2OBm3bQ":4,"Aalbsk2pFczUedpRWKUyPw":5,"Lq0kV5Tp6QcAMP-OOnHCtA":3,"zBGfa6Vx4K59v8OR81gzJg":4,"3KhqskUTVyZWJ3LIZ7zkAw":5,"N0_UiTesa8O4WQSvIMARGw":3,"Lm4rjgZlTtLfsriICKdD8A":3,"X0Y2cK7dtELXEqkA0zEBIw":4,"H3oNY9CnCwqHTU5QMHEdew":4,"MjHJ9VOUywUWtO5uV4RnZw":2,"nZLnmN8flT0WRP2r7yDCOQ":5,"x6BemTnk7_eCuvbv5MflWQ":4,"rK9wysMZ3nh6b6dxiG-l_Q":4,"_KGe3v1OzRnUmKhb3VkDgg":4,"BpMdiKy1Pf5VdBouzuui4A":3,"5cA0fBYsNagnDot1AATykA":1,"m79L5WLftprDSKdXEtdrIg":2,"KUdd-TYkyPbxSJkMQ3FCJQ":4,"adv1-kA6k2N4L-e4zULuNg":4,"nmj5yK9dZ2atlM9RYDCRHw":5,"7mP8w08JiqlyDzdF-Ui62Q":3,"oyzi74AxIx4Ln9R597F9kw":5,"trG1k-K6Nq4YKcexa1AGOA":2,"7K3xiP-5sj_x3QWHlIFFxQ":3,"c5awK9N87I8DiEvVrNDEMg":4,"J9vvI2SEhy7yWnNPeVPdRw":5,"jgWAgT7LWPTf5wju9Q-kiw":4,"Lnohr9bpCbHNsomazXDg-w":3,"2E3RwtfFDrxk5qEezocP4A":1,"dx8lP_mmctRUFFz5Y3xpOg":4,"Y-bDtbLUp-szo_WxL883-A":3,"WHd8fLeMeWKUK6sPyeB-UA":2,"-tBiXT917wKlr6n9wSqViw":5,"nMHhuYan8e3cONo3PornJA":4,"chFzObJSoxAbVlFfgk5JRg":4,"FT5dJ98SYbGE4ULtKVkW1A":4,"nvaAUTTl7oqiJDhuimNG6A":4,"4Zu4QUdbM2mIdBRZmbf5Gg":4,"yMhjh0ASFZscz0QlLxAj0w":4,"v7OwbHgNgy_VQ9eP5FjvUA":5,"WF_--gu5Z9WB3CU2kJQlfg":3,"BPN8GzoigZNQHEve5iP-gw":4,"RV9yiJmJNEpFv-CqgOo71w":4,"jy4-gm73tseqSvtqSt9pZA":4,"NUR1pLEwUETAvcW_1rfGFw":5,"fhhe2udVfL0V_9_ocPHWKg":4,"2RnxG9v0fPngep5M2UajyA":5,"-g5leVOzKA33Ruabe2Zo9w":1,"OBUbR8vRZ7RmotiwvBlVDg":1,"5kuZhkdpKKu9d_dTflOh4A":3,"vU4gIa-uid3K_Oc9dZiclQ":5,"ahKN6wh6z2vZsd8C7AyG5A":2,"eb_BJXIPmpJ_zad4SN_Cmw":2,"3f9oR4imL5js4nMPvNIauQ":1,"3QPwxHWoiwTXscuG7_jecA":1,"gmWSXOysesNdp58WnwTA2Q":4,"FM9Wf69gZS2nHbgnGlh6mw":4,"Q337sJLaPPiKCsoIoSEWGg":3,"zw2iJahOnSxlzmRlF4al6g":3,"4iJUNAUVYNEuh16yK6Virg":4,"LVngid2NNh2s5cAjuOw6tw":1,"qE8YEvUZvujKfWZj9T6oYw":4,"t-KxQbLl8Y8FKsXmpxOcdw":3,"VDzgxHjMJj-1nMfJMtcSPQ":3,"8HQ8clouLGgee99KkR4vXA":5,"ke3RFq3mHEAoJE_kkRNhiQ":4,"aeylHhet5Sfqe9uMrD9IhQ":3,"TBqAOlyaTRaFd5sYLAVoQQ":5,"AxdOGtJ8bJmL8uXB0AQS5A":4,"AIN4FSq5ZM4Il5BzXzMNXg":4,"7H0nbExftMZlpZDXm0QrBw":3,"o-OV2LkJxpcCHmI_d4TZiQ":5,"cVMunlva2-PmpQQCfLVxUg":4,"Zx8_4zKdDBSO3qGrkukBIA":4,"08IFR_ruWR96K3Q6sakI_g":4,"KECPmpLZxwroxLeUy9TDoA":4,"WdQDc6mBTy2g90nxnjMzew":1,"paF7fjuCWbqg7pjwSWnMkA":4,"dUi5Lg1Ay3HwK0p_ZaXNYg":4,"7tPe20uDErh-iSkfNEWzVQ":4,"G4ZZHlp6CdYBZOirW2_PQA":4,"DF-7XU1Wncxx3XqZoiIIGg":3,"VpHNYumY3F92a90AArkFyQ":3,"KKNaAQNJmJI6bKxycsuSZw":5,"x_MCZPQ9G-IsDnwkJBceIQ":4,"2wRTKKFa9GZI0Jm9WaohrA":1,"N4SvPGzNxyjryabf88PrcA":5,"h2intC6yZX5pwccleuOriQ":5,"BAbYfKQaQImLil6xqaOFyA":3,"ppdupQ9MnvVtDTWWW59NKg":3,"qn_JH7PPnJzwWkiAhadnsA":2,"MIgONuEZlXLyQ1xwKAwX0A":2,"e8kRfAKXM_1qj9LMgp0s2w":4,"zOayTVSvtaWDt8pWH1N6OQ":4,"-dunP-FvJHpQmx5qt5Qoqg":4,"JRzrqJmsQ5AZ4bMQLUfyHg":4,"WBxuIQsxGl7vNe5MXYszCA":2,"-cy8EpdXs44iT3FR4En0QA":4,"LWY0A6hWUJ8o3AIKGYs3Yw":3},"5CTxY9Gd6gJBIwdqvhTubg":{"WmUcv3Pvoc1DyhE_HMNPKw":5,"iupX3nvMJMiV07M3VKVl4Q":1,"nREHMbIzWdfWtOh4l1bT3g":2,"3q5THOSYu39imB8tGaieCQ":1,"kALWQ76kSTrt_WhdjLAs3g":1,"DdvIUeFlPnDSUKEyy10hUw":1,"8RCXoyRDdc96G2mUDkBLRA":4,"yVBDwXTJuhcWdQirPvkPGQ":2,"gMVWJi_dldZfofI7EShmNA":5,"K8dQr_82-DMpDudEv8PDmw":1,"Rer910CgwICj8-B1gmc7aQ":1,"_ibKsVEx2LMobFd52D0NZg":4},"eMWZ2mRO1dP3sdr9jYrwXw":{"fO4Da8qQtt7pH1WmLWRPvg":4,"IRQNOYVE-AyjCliZa_3R_A":5,"DqY2VlbRuQ3Mu2mlxd4xUQ":5,"Lz4e2G6rzWd6olANPzXvCw":5,"Snvt71a7KDWYxeltag2zLA":4,"32tIoMWhcnHbGc8olwiP4Q":5,"eWPFXL1Bmu1ImtIa2Rqliw":3,"cTz7lxA0AdWKMba6Bvsi3g":5,"VxV3IHS33O4ha71ABE8J0A":4,"8RYf6xuRZDTyvX59eTAydw":4,"jf67Z1pnwElRSXllpQHiJg":4,"oQfCWtO5-fGTFrclqCJOwg":4,"oOrqgxKCNuPwF3mlTBmgZw":5,"E-ads7TQcLMAoVp-H311UA":4,"wXKNBXkSlJsRz5ONFnEp6Q":4,"l2lpBXx8jKl87J2szyJRuQ":4,"kV768Ru9q3JKNNaKuKAKCw":5,"BIDo9kJgny-n6XlBkGlrmw":3,"Fh6OndE60vzvyhCX1Wg7Aw":5,"Jlcx_J7DAqXthtsb_OMBEw":4,"5FLRsYrT6w2VSDvQDhphXg":5,"nhToFLPoqNixNbRK4-xFQg":4,"6ii5JM4zVaonwvgVcj9mfQ":4,"rmiK8V7l7NgEJSHJT-zWQQ":4,"XZc403LVGPuIHCTQiZHlRA":4,"vhcxvOt4CiF8_NJz5kOHRg":5,"PmeN_flCu1DonjP_g90sFw":4,"mPDE4dMqAyLZNCR-tEYQ5w":5,"UIhFRsZoPTWY38njcKKWiw":4,"pD7NzevYc6HhYu13wCxiiw":5,"6hLmXrcXELRt1_H1I2mE7g":4,"W0TK5K3VLbnNrrzLTaaykw":4,"m7icEOgYpM3B8TlbYsKPzg":5,"6qXQQOWdUZiJmWVqkWB-3w":4,"j_3KufSCgZE0fOYjJ7ZCNQ":4,"aM4c8qSzfJeJSApfQWz8IQ":4},"sAI5GDcSlxmGr5X4EFk3jQ":{"6VRbbNQe5ouWmwsMebUMkg":5,"Q2u3sUNNDHfPSgoj_V4uIw":5,"_1N_1j6LNfs6fSgTkhbXzw":5,"Dy7TJMsjsxMLmXPY4kNmcg":5,"2aryhhbk6pjj4gHE53mcag":5,"rrWhi2TL0smrbihvavZxcg":5,"Kkjnz8XUn3ljW8SzW_o45g":5},"hEk0VssowoyeEF2R0ZB-7w":{"d6eqlH4tKE2VmiTPN6TOEw":2,"Lm_mR5xDF91OeZw97ch41g":4,"x2ZMAyneUiBD6Sml0Fv2Xw":4,"-vVQyTVHitF6TOHGijVXxQ":5,"C4GHQTB-G0R2Geov298GLw":4,"kGLM7M4G9LuxD9Y6p3NSPQ":4,"rR_szXNwNQB-MgEoTElb8Q":3,"JQJsfuuF0F25Oo3AMUBJHw":4,"DHAq_WmQwjk7gviKXwqnjg":4,"zUzEjxKEn8eNVksImZ2oGw":5,"OxIeMVcop5oxBUWANi-1Rw":3,"iTSuk8UQGaNAFKBYEzdeWQ":3,"tyXvO1G2qK3MUfaap30auw":5,"IUnRnZHmA56Tgr2acpHRow":4,"8ZKrJs_z1Wfbb9yHKrwinQ":3,"5kD6dP9etfUqtyXUZu9ZyQ":5,"sF8rL9XOz4v48YdTucaBGQ":5,"utIjhLQ4aowlreRuchFpBA":4,"kc5gJPisT5L5z8lLa9FV9A":4,"I9IDCNPrOvJYavtsH936cA":4,"3KCL_Bu8mOk-h7Bp-IXL8Q":5,"vgXE1I7c9ElcfYyZfQiN1Q":3,"Zg5JB5GBqhmxt9W7tFKN7w":4,"GVYP0ZIYLGt-8Rh5L19XIQ":1,"cQk8pgpxC-9MzFJS7Zo45w":2,"vpr2y1e3VFRSg6UszEuc0A":2,"lGJTErTf8Y72U4OLHhW65A":5,"NeUf9FyCCIN4MEseNyqkXQ":4,"v3MGJBF1Mc61KwgqiIY-uA":4,"NEdZVFD-w-96pje_ajFalQ":3,"mDOBApO3-M2024kWjhMNDg":3,"w6bhabpSWS5qjFb1AT72vg":2,"NjWAVjMxUwOqnpOOQL71QA":5,"XxhYW_KQwQk7As-2sVelhQ":5,"P4Or3as2jJGwyBXIZ_gxBA":4,"niW0ggRVPW5fafcfImdK7w":5,"X7844DdJO4y2oVbcpxD-NA":4,"6BkbwY0j33py_XmzvmnfXw":4,"y2eo_MWD3XfnxxvhXh7Esw":5,"p1Wb4mEH04qrUMfmPepFzw":4,"xE01FGtowIzIEw5gPLUh_A":5,"UQSGL98JH8346Uv9B9Ec0g":3,"wHi8ODv7TGmeUB02XoX-mA":4,"bwu0cUZfksuu-uzTPrrl2A":2,"SsGNAc9U-aKPZccnaDtFkA":5,"wan0X-oHpLgGTPXqaICZCw":4,"YRDKsBFYP7G0E8BLJKIkvA":4,"4O0GslAIwG_1regXO_UcaQ":5,"Z94doPdgyDOgjtYUVRBNjQ":4,"ne8o0APyK1CL_BLhDGbRsQ":3,"TJo0LRUmc9Y1J05dM6fqiw":4,"-b9ZUSmcsGxutDSW1DIbdA":1,"-vI0zsfDrJfTjD7OXoQJvQ":3,"nBl_NeArpL08MpoghDiA_A":4,"V8jMEIQ7oGK-vKyg0FiTCA":3,"W3UMlRDOn9Tzd3kfYlHX3g":3,"cjD2yGRhT5yaSj_KP55Ptw":5,"EyCTFYEjN3hdKyGLWjm6HQ":1,"fvhWfSPlx5J_3F-ScLpvXQ":4,"UK51LgJRJ8_LUQQPZ5zfxw":4,"TqkBwRmoEgECElxeY0OgKA":5,"kOY6CQ4VijKg8PnCUsTXgg":5,"XdDSKZ_1I2qP8QHrrwmz5Q":1,"tivpU-VNABjNlHZ_sMUDGw":3,"41CXLCeB8z2oNdIOvnrzIA":3,"PUS65BH7urto4zhUJ5Obmw":4,"coo6eAhevrKNC1azLAfGaw":4,"wUALXOAurB8LfKZPhLfjZg":4,"jCad2RCY5BT0ZZhk9r1ivg":4,"Nui7Cnhrhrm4Ar2rcSHbIA":4,"JuaQPvvWdbJ1B1Tn0jIt1w":4,"pMBxvWFY03Z95jNVUVWGwg":3},"ZfDBU11iIuYxqpVe_Hnqew":{"KzNfOL7OtUVwMxvJZQIVHw":2,"AwD1zOOhuCAbAPSaZ4X68Q":4,"34uJtlPnKicSaX1V8_tu1A":1,"UEUQS4z7s-DRzQjky92KYw":4,"nZgYNbl1XlZyyKlISMoG6w":3,"rP76z9iDOFczywAiee-l7A":5,"kEC7OlpPnZRxCUyVwq7hig":4,"5GKbGn9-fAgQ0njSh3OJ8A":3,"G0nUhYF2q4tnoOPwCjXLig":3,"eWPFXL1Bmu1ImtIa2Rqliw":4,"8buIr1zBCO7OEcAQSZko7w":5,"gGeVLZ9j_wAYKbaqgnKSJA":4,"xyTJYlbE_MLouK6rCou6zg":4,"ASOiJ8MmbBTgK2D1_MQrqg":5,"EW8rqAt1czCzdKi8g9P5dQ":4,"kV768Ru9q3JKNNaKuKAKCw":4,"Kx6vAKUcy3wPhw3K0W9LKQ":2,"f3EcPjqKftEznBSs2oQVRg":3,"KcSJUq1kwO8awZRMS6Q49g":2,"9Ywv51iCL_QSIGzFA6vqiQ":4,"mVJIPDv-qfYlatHYeP_saQ":4,"jmgKs7CTqSWWwJnFnPIf4A":5,"zAdtpqh_rVvAMwc6o0t4Mw":2,"zObyDUjiXSTCXa5t6w9ghg":3,"f6KGn2OyYk6LWEpnUEgerw":3,"MHajTmVXiD6hVBYTLTwo6g":4,"3rwM9fPYPk9qDkEBOhyHbg":3,"79EG9Pv0bxNTmBjTVCd4CQ":3,"pCSbslNkq0fL5ZZ3RhUZMw":3,"Xhg93cMdemu5pAMkDoEdtQ":3,"XZpUbduFE3HUbFkt1Zk3aA":2,"m7icEOgYpM3B8TlbYsKPzg":5,"xheJf3qJLLf4-Ck8ay3GFg":1,"M2SjLXsuAy5RNKwxaA5E1g":3,"Ht8mXLuqJSTPrU9kvzosUA":5},"6PIJYWldEW6azGogMjPM1Q":{"7q1FpSXbE6XtLNg518pxDA":4,"qth1W742hXtFoNVYvuHBEg":5,"YY1UCrnuOLCTxK3mKsqiDw":5,"XQokPEF3UJU2CIWj8rnv3g":2,"AtjsjFzalWqJ7S9DUFQ4bw":1,"KOOtk3mhxPoJtjGGtP54qQ":5},"W8-d_5kpVhwzyaCOfDHi6A":{"6UXw7_U13Th0PZlMXZbjMg":5,"YGH3QjeDTLOsUk5xUH8w8A":5,"RHIIMuvu6xPNHxtZv_QWHg":5,"2sn5BECdlYxqQlw1VODDoA":5,"u7E7_VtKhGBbH9sMoIQCIw":5,"jf67Z1pnwElRSXllpQHiJg":2,"1U1GRksKXF7q8FKcW0e5VQ":5,"vP4fFPb7YnHeDgYWjJFPjQ":4,"UpmWA297Ax4q_GUKkJyy2g":4,"0jq5ZFLRqAAujEuymdPu4g":5,"V_rWghvlKNKjARY6rctXGA":4},"LqrSG5inxt-fetAWeMkStA":{"naLrErBuJr9IWd6_rv6-XQ":2,"WnY4HPJIYNXOPQH2mFzl2Q":4,"N50HceZf1595UtU867u4uQ":3,"qt_GH5ZBn6xT0CtzNdrvyQ":4,"5GKbGn9-fAgQ0njSh3OJ8A":4,"DJlb6DLzT1yK5ipnL2I1dA":5},"l5upkLok78p-NQN_3uurrA":{"rDvz5jX65gpfONFu7er9Tw":4,"enbTOcl7WNgsjsAtmhvDRA":4,"pkUj-lZb5ZEzLBw87-pOew":5,"7SO_rX1F6rQEl-5s3wZxgQ":5,"JDFmfsK_i20VFXbGE1PRVw":5,"85mj0eX_C2wKCSSaqO1w4Q":2,"DlCtdbceo4YNSI53cCL2lg":3,"m9Wqqma30o-hH2fAX7dnug":3,"D09yG6Z3gcsh24Qn7Y4gYA":3,"-DGbZCnfEiHUy-ksKeJ72Q":5,"w19cemjVR8u02PgjFpJ7Mw":5,"eg4nd09goZ8opkthsKgn5Q":4,"8dlyEiypNYB0sVfdzQll3A":5,"IgaruuknYwCr9afeDYQ_yw":4,"8Hn5X1AqgmSLHRG2KgBJBg":5,"d2AeNB4xw67E1Bzpo1Pm7Q":4,"4AKcmN--0hbF0kX9pg8scg":5,"fEKZ_IjfwtIuKIcuZzUJJA":5,"1NZLxU5WvB5roPFzneAlLw":3,"JokKtdXU7zXHcr20Lrk29A":4,"Hn7f_Gh5ffvns_7nU4Wqxg":4,"-sC66z4SO3tR7nFCjfQwuQ":4,"Xo9Im4LmIhQrzJcO4R3ZbA":4,"Cp6JGY5YIRncTV_My9nf9g":3,"dcd3C1gWv-vVdQ9XYV8Ubw":4,"m_rEr3Vg1-f9Dg-Nag4FWg":5,"XmDiFI8SuougNUi02ZCdwA":3,"H83uIqLKcOSFcmJhXmc-lA":4,"eHC_xNrT1SkJyC2oncJlhw":2,"xcOncADGPr9eki8OU5Ln7g":5},"9VLkQJJBieggMLk_3l5FLQ":{"VAeiLMTICw2CSFpy28CsWQ":1,"09qbRt7T0CHWwUTHW1VO0w":1,"fCkgtZUUM5qmU_-KWQiJuQ":1,"PXviRcHR1mqdH4vRc2LEAQ":1,"v_bwANH8dZKsqpM_bIzzrQ":1,"lliksv-tglfUz1T3B3vgvA":1,"npfVfumxVAkQNYpY1fSvew":1,"mUscn66rVwGRY9rDdtuWag":1},"fW1ofml5a0cFiE-hPiTkUQ":{"Udpuw5x3x081pXnkYvbV7A":1,"mpDxBBGywUE6GRRKja3sBA":5,"UCzaZ2z6E-Xy8Vn-MLpIrw":4,"k_oGELzpHDK6JrHRsCD2lQ":5,"V9euJerhCkh7PXKjtsE2rQ":4,"L2AXPsl-AzyY_b95moUexA":4,"Iw_qZEDbHv9Jr4eC_2lfKA":5,"t65wgP7lQrCqxjBpMwOdbw":1,"atC08JSxcbm9HzU8eOLuZg":4,"yTDNPDu7ZPRO7vV7vc6-Dw":5},"THr8peJ3dxCXVgPlKjagHA":{"enbTOcl7WNgsjsAtmhvDRA":5,"V5dffroIZRH_JjxIh98y_Q":5,"qhIlkXgcC4j34lNTIqu9WA":5,"pSZEzEgvzIG4UcMdNBa0hA":5,"LQGQ1w4pYrf5in6LrU0BlQ":4,"YUcsW4G5SqZUmSqvFXdUKg":3,"zDfs1Kyk8orFF8bRnSPx-A":4,"WjtJAtp19nA61b8LT9uLrA":5,"SDetUVwhaCPGkQYqmUak6g":2,"OYCQb_5go_Pgd3mW-aIvCg":5,"7lSQXiyPGrtfnCg8ym1Kmg":5,"EFNwMxaajz779YWCRmZGIg":4,"2lWWQWdSVwT7KHrtXFDHuA":5,"1f0g466Geu4nDdJhYQ_Vhg":4,"kaIue7GRCmkPzDeHDBTttQ":5,"nbCAnw8b9_3EaSPpEfLd2w":4,"-h-q6zTIdPlkz9BDP11sBg":5,"NaIF5ywG93q0i25czpCgLA":4,"3Zsjlum5kl5N5KV712aTMQ":5,"ObnZiF99lqggVasgyGBtVA":4,"2va9Ql6OCNWniepqb0eLlA":3,"-sC66z4SO3tR7nFCjfQwuQ":2,"Any6WyiVNmgbnWLqoxPXgQ":5,"NqelJlme2RN0RxcmO6lxmw":5,"DTFy9-NuZBjBEd9Zcoo94g":2,"uYf0LEYULK_E1eymdMEe0Q":5,"RySnetMQUJKbbtliTt4Nmw":2,"41j3GB7M-Lwq284Pfb9zgw":5,"cN6aBxe2mQvrQlzk26LyRQ":4,"Shl6PtJERnowSJSC4IHbYQ":2,"tiDRFqv5ms1yuj0omuVRqQ":1,"qz4ZOcv-840UjfCEYI4qZg":4,"YKOvlBNkF4KpUP9q7x862w":3,"UrIT2RgnCg3OfRBr9J3h7w":3,"no_FXjscklz1SEzM_XnVgw":5,"C90nLkXxPxv_1y7cL4a_7Q":5,"4sW8Z6NLXLRkruSKSKUEUw":4,"MDtjD14H1sGLc4tSg0sUhw":3,"BVo6wBuFwPH3QVqs8-JEDQ":3,"q0PuwC1Qm46RWHE9tmQuQQ":4,"QbQTT6NGr2bFxGAdvKvMSQ":1,"rCVaj4xZKS7Af89p2JjcpQ":1,"6imLt53br7SJ3av07jjH7w":3},"fHBD9l80uh4zy_-8TSOPqw":{"Y6YCdd7RrTXpGFoACkyGuw":5,"rN2cc4bXzlsIxhWEoolBTg":5,"JKMGWsZVdKrZ841foAMM_Q":4,"XdwhxsSvZi7ej2WAQ_wmxw":5,"LQ8xiZao4z6hn_l1qy6Jeg":5},"0VliVcQnYUaewbsgXCXMdA":{"cIPE37nO7qvo3t1I15oO3Q":5,"8ktREOIxt3kRdJpJK7jpfA":5,"5D5DLnLMYiIt2ztgp6rTqA":5,"DfJRq4pqowfdTB4iTAENjQ":4,"9QRits5JGrMffJFirMvJBw":4},"xkTbpCc-YhU8-EXZDA7u0g":{"Ydc74ermKp1L4fYOrPvzXw":3,"tb24fvNJfHhyKEXkKn12Xw":4,"X5QTGpPfqXFtmtizsGAksw":5,"opyB7d2ar-rrWLR4RPsUPw":4,"Mng1FUcW-xRSdsDkowQm2Q":3,"WUZxVr_CaRqEQgzvyeK5tw":4,"zBl32GAjYcKNpsEGPXXuqg":4,"FGePlnlKXHxBrxYMNGtdAw":1,"GAPqG0WNBBidKeZTMpEZ-w":4,"DmkTDze8ruJr6o2f5GAvJA":4,"KOpBLWlI5swLKOq2U0vsoQ":4,"xdwPHc25l7_roZ9Kfea13w":5,"Kqn4J9NTgZdMAnV4HuYh5A":5,"Ase-gwT_0s4Wfv7XWXzE6A":5,"LzNJLEIo4gh-X_rmDkNkNg":4,"L3BSpFvxcNf3T_teitgt6A":4,"wwBzSIjLdQl99_f4ToFLMA":4,"xWcTt1L4vQC_QkPfPBVlCw":2,"5vbhAkrjd0E28Zl1IfHOWg":3,"jVgtPnzXvZQOCCIUPEBktA":3,"rQ4z0EStSZE4acgkne6Hmg":5,"zmFc8M-hS4uuyY0hklIpoQ":3,"-1bOb2izeJBZjHC7NWxiPA":3,"MMLEhoPYQif2PEIVxAfIKQ":5,"6rijZ1qIjiq1Dgdy35iqxw":4,"WIcDFpHEnC3ihNmS7-6-ZA":3,"3n9mSKySEv3G03YjcU-YOQ":4,"aRkYtXfmEKYG-eTDf_qUsw":5,"FeI75xIG8PF_XZ6P80gLBQ":3,"ZNi59SPFF2GXSmRrk-f5Rw":3,"M6fjHpkL9IRI-nI0BattRw":4,"R2IWbpUgJQ3NRRjKQy6O_Q":3,"M8h8cZ4YYFVH8yNHZuKIVg":3,"I_N5b-CA6j0TFMpy1xYKdQ":1,"H6F8CVOFILdnSUQtmvy_zQ":4,"V2isTBBfO0NgLzXO9oq1Mg":4,"EWMwV5V9BxNs_U6nNVMeqw":4,"V1nEpIRmEa1768oj_tuxeQ":4,"sjCRI-lCh4KLO_RYQdlEeQ":4,"5pgzTBgt-HR_0s7TDXSL2g":3,"7_7fxuG9ESAFmx-AiMsJHg":1,"r3r_bAfa6pZKIhQB82FizQ":3,"tz7FNOyd0QY6f1vudq8Wlg":5,"IVc23uY-36WUNYoIbz42Fg":3,"c0zhbiffge6fGl_Nzgxbqw":4,"d2AeNB4xw67E1Bzpo1Pm7Q":4,"pQ3kRVmttsV1bHxuTf7TAg":5,"lktu5JPDlQUG-7cV7gOzDQ":4,"xCryT3Vzk_RLIkhiuUJwjQ":3,"x1yYMaZfDVEp1dW7JI8eJg":1,"RS6V9TGTLQmBRuXsmWCOTg":5,"7cP7WFmWiTVh-raIL3N_Vw":5,"ObnZiF99lqggVasgyGBtVA":4,"CdqTxe171tKTOkk8T15GGA":4,"FnX5RbZA0Pv546dMOUDAUQ":4,"M8v_fUJM2wr4qrCYCBJHNA":3,"d3MxUXS1b6U2P_gGuCO1-A":4,"WJ5mq4EiWYAA4Vif0xDfdg":5,"4tq7gtfwhEEU8SDHXRASZg":5,"YRJKTPc7Tkz1cbjGHmOHuw":3,"ntN85eu27C04nwyPa8IHtw":4,"sb4wU69LkCtC6Axqcd34WQ":4,"ZoQAOnEFnyHjSpomtfqesA":4,"VC0VbRhQqvXpolK3pFuZPw":1,"QnAzW6KMSciUcuJ20oI3Bw":4,"uKSX1n1RoAzGq4bV8GPHVg":4,"OdD1GuGNQ64ssJmMJ_D9RQ":4,"QPheu9dnwdlaPwXofP8ijw":2,"LdI-fcJDXGE7ns_jwWY2ow":4,"6eax0w8j0tudDOkvWgmQ7A":3,"0G-zqtH6hRTu4uxRwA-Gpg":2,"nQUsMhT7qY6pPMvTT6xGcQ":4,"Y-9dJvw-J2d9QKfuL7mKgA":5,"6imLt53br7SJ3av07jjH7w":2},"BAwxDvddcCjodBMLd5mVFg":{"eLPld7Q17XxlclFGzZQX5g":3,"c8Xamwyv5Tyi2VjjyQcwaw":5,"tMpFSMGrXz8dzvB9UZ69XA":4,"Yq8LiVymGA7vBpGCQuDfRw":5,"U8RIy3r16fmuneo2stVuOA":4,"N_AicjXIG4IJFzJ-Fzf_ng":3,"kNGWOprBFnteCQUGpLnM8A":5,"K2ycDEk6_bTjL6hYwBSpxg":5,"6Oh_zSwy3ec-ThAqHqGj9A":5,"IoLpMyOXR73OlQnjjPUA-A":5,"YgNhunvo65zAO1FqS3WdWw":5,"ByJioN1ISBWpUSAI0rWt2w":5,"nZww1gdBAi9HtRKiQHL2qA":1,"mq2tmmgQXfo-3Dh-xOTx-Q":5,"HyfFenprdpIA4rmKu6DW3g":4,"IdpMuPyKIEfO41IlLxXwmw":5,"OKl4Qdg_zAwpQMhshD_0Zg":3,"c6op8GXGXxzeEvl3C3mPXA":3,"f9RASN8KvBGs9feNYOluiQ":2,"Tc--MNuXGt6ggLzTX4LnOw":5,"ZmzjoG4-9Ix50l4mNgB9xg":5},"n4B74zbxZijXgbbWL2k8yg":{"hEVQ4Zumf0QLKJXBpx2qEQ":4,"GCTDM94HiKxC7GcAWbb4Og":4,"9snofF5cUPE5RoGstsNkAg":5,"KZwhEVrTWdriiwzHX8aQ0A":5,"NXvSn-78mqOK3mBJpVSLZA":1,"0IDIy6Ti9V4rKhX-WgWFHg":5},"LSy33vnFSr-gFV9QX-7rFg":{"tqu42L0qXzkvYKSruOz0IA":2,"nREHMbIzWdfWtOh4l1bT3g":3,"HbUQ_3dlm3uCacmhTEMnuA":5,"KpZLxHrp2PIP8tLBsPLiww":4,"Xhg93cMdemu5pAMkDoEdtQ":3},"taqPielpA7eXixxxRR9OgQ":{"1V8f3A7p3HV2r0BgAbqvaw":1,"JokKtdXU7zXHcr20Lrk29A":5,"7Q19H5nM3oFRyCg_j0QV1A":2,"pgz6IeaZgLuzqrk6HMPhzA":4,"8_wUsDlOE8Guecq5RZZjDg":1,"oY71G_AaKlF4Il-gt4L2OQ":1,"Pv__E1amE9nj_jOYrAoKXw":5,"te-5x-HhFgSWwBkGSG33Kg":4,"u-vrEJXXTmj6I1d4Nv6EeQ":2,"B_1LLEKSddI0hvOuB6S6VQ":3,"D0PUyt1EbOJKdLh636hwWw":2,"nIX7WiUPekK5YpiRQorxlQ":1,"VVeogjZya58oiTxK7qUjAQ":5,"7QeXmpR5gphG5mLJuAUy8g":3,"9tSHBEoAhKu-tkU8n6SKjA":1},"5bKR551WDtbq9AE2Y1guhQ":{"tFU2Js_nbIZOrnKfYJYBBg":5,"4bEjOyTaDG24SY5TxsaUNQ":4,"2e2e7WgqU1BnpxmQL5jbfw":4,"yt7Ymiru4YanpE0xzzDxrw":4,"CZjcFdvJhksq9dy58NVEzw":4,"AtjsjFzalWqJ7S9DUFQ4bw":4},"Pkuj3s2T5KUGs6-yOquh9A":{"BcgeVKa6S48N2-U0IfM-VA":3,"WS1XuIez_2KP-3RJD-r9kg":4,"sIyHTizqAiGu12XMLX3N3g":5,"WqdCrAhYSewDAom1qY-t_g":2,"yxxLFua918P53BQADGCSCw":3,"2e2e7WgqU1BnpxmQL5jbfw":4,"wZxrcIHmkhT4OHvIxPwd_A":4,"NxsCqQCpofRx08m535JYIA":3},"fBUX2UDQQDrrYNq9Bxft4A":{"EKzMHI1tip8rC1-ZAy64yg":3,"7QSYBp2-AOdyUJXEaLnbgA":4,"BXYK5ztWpJHKgpwNCG8shQ":3,"yBv1gcLXabzlGvZNs2sxug":3,"o1GIYYZJjM6nM03fQs_uEQ":4,"MuIXnv7Oq7X3-4aEsp9dDA":3,"9VYZA4vEKtT_SXHj-ZK_1Q":3,"jGyJnMnBN2KQ2Px8QcP-_A":4,"1CG2E8Qd8bas91zCi5GaFg":5},"l6av9UfDeLUdrJm1wvzJWg":{"7q1FpSXbE6XtLNg518pxDA":2,"8oqcpmXrymQ1RRMK12S7QA":4,"QgeyXkZKSOIS_85pDIVuQQ":4,"YNx5vtfjtwXZEk2kBQoA9A":4,"pALpJ6xRXPgBNw2s3sDHxA":3,"Sz46GVteyTbGQhA76HmleQ":4,"b25jGkZerj2M4WAy95n1Tg":1,"WnY4HPJIYNXOPQH2mFzl2Q":2,"k7g41CrVComlOhyZaM_2_A":3,"UjbPHhzyJySPyuqekR73Lw":4,"WEKQZap6YHcU25b6kIypNg":2,"lyC2KqGiFIwct39jbdIdJg":4,"McbAumPa42A3mz7VUHjA0A":5,"9u8OhMvCwj4T4obO15d5ng":5,"W4A_cYOAHhOQ-wb8E7suvg":4,"jBU3y-V_F037YdTWuqF_uw":4,"t65wgP7lQrCqxjBpMwOdbw":4},"egYuVKo4P4kYkocJ5lhrdQ":{"_OYlq2UoKPQO_ElqhC3a8w":4,"uZPVyXLyC26VaJRAZwYmrQ":1,"WYk91WPklqRWuk9z9DsPDw":5,"utVe80w-NAj9KMtIwJo22g":5,"HxzCCUBQDCM2CaHOT-yUew":5,"oJpmYvLibGrYPDvcaUeMOw":5,"3SlKa69UVN8KKYYPtlz1ew":5,"5kRug3bEienrpovtPRVVwg":5},"XNyBDyWMdeqFybcCi1yy5w":{"DXkZRQ--Utku9wYbZ97Yjw":4,"a4cMKOjdVLTmJNhRl6-17g":5,"USyDC-cZCexcyNGrc8uiag":3,"Es300Ys1XXPYg8aI7BKVYQ":5,"AtjsjFzalWqJ7S9DUFQ4bw":5,"9_HsCjEELmey18A-gTzZKw":4,"JZWCBnrqU27DF8SOQq5yrw":5,"eq6lQI039SBLC6sHm3idGA":5,"Xhg93cMdemu5pAMkDoEdtQ":5,"QbmcCE_cLq4WO8ZMKImaLw":4,"W0TK5K3VLbnNrrzLTaaykw":4,"E9ZsPtGovfEPHlMHkDdlQA":3,"Tr9fiwgB25qMpya6t8TIHQ":4,"Ht8mXLuqJSTPrU9kvzosUA":5,"RE3xkxkjmHQIARrLSIeerg":3},"ZVBvgWyq0ZP-Td2SXMeDAA":{"rDvz5jX65gpfONFu7er9Tw":5,"gWP6ofoyTbK0SZj1i_XqNQ":2,"Zx8_4zKdDBSO3qGrkukBIA":5,"GV5kqyrnOTdVr1VEd-Ji5Q":5,"b78Cnqgeb4GoHqPobBXsjw":1,"rGDtWLAVg3e38S0PDtmWWw":5,"Fb5ZL4VkO2Yfx-bNJexAkg":5,"QNo69O4cy6a3HGb6RrGWzA":1},"0pjUOShqGTqCNqpIPXSewg":{"eLPld7Q17XxlclFGzZQX5g":4,"gkWEjZIVcrUerEzed6IKpg":4,"7q1FpSXbE6XtLNg518pxDA":4,"AeKTQBtPRDHLAFL9bzbUnA":5,"npfVfumxVAkQNYpY1fSvew":3,"I6Og6AURCkhvsUuZclZOQQ":5,"SsTxjxo8qvqBMvan1rzNzg":4,"cWFpyN49FRsFrNd3_cb50g":3,"kALWQ76kSTrt_WhdjLAs3g":1,"eq6lQI039SBLC6sHm3idGA":4,"QbmcCE_cLq4WO8ZMKImaLw":3,"cQJM8VpY21O3HVu7j_b7Vw":4,"otcGBl0p5cTCfSOr6O7PCg":4},"txIED489UiyV-fqYLt5r6w":{"LCeF1wK5OqP3PPEVBa5Xfw":4,"OUpcKYGbVYgSS1Oo7aQ56Q":4,"SLyacGZuMUKqrQJEooSkjw":2,"rBPQuQgTcMtUq5-RYhY2uQ":4,"2e2e7WgqU1BnpxmQL5jbfw":4,"pG9AXrNWpjhX8p4Bz7bLrA":3,"4zuoTWrEps6SnmyyS8UhYA":5},"wRfhnloTj5sg7EHAkJlfEQ":{"U6stLkJYMaro_4-3KI84_Q":5,"3w5gd4EuSc75UKYMJiNUPA":5,"YacTpiq0ZptFcXD7I-kdGA":5,"g_xxHSr7uglGfd9tXfyHkA":4,"tcphcsPONrP82kUyvcELoA":4},"uf-5xyfJsF5t2lNjEGNxVg":{"H_SuH7uLiYahDMbNBB9kog":5,"xxOQ7h6s3InV8o8DOVHlMA":4,"3fA43apyr5i8PAm0Az04hQ":3,"CZjcFdvJhksq9dy58NVEzw":3,"dGMk9Rg32zHoYBKI7zPsrQ":3},"rVvflbz1venrgM9eVvMyqA":{"DO3Gk17RyJVW7zYMCtYPnw":5,"-7yF42k0CcJhtPw51oaOqQ":4,"8Im7lMgIWibDBnh-2E8c2w":5,"feAhN6tlflC-DcjBWxmOHg":3,"Ws-vsP4kJVEQC-UAzAEyWQ":4,"73vkDcVCbAA_ztudgETErQ":3,"FAencdv8yZkYi1YGdX1dcw":3,"DrZ6gS1LNpMgy4f2zumTng":4,"5-0gdwFcauZ4wmr2DElnQQ":3,"oFvqnJNxHguP3iBj-jZUGA":3,"2_aLW3fpl2uGZO0go7ExIw":3,"CRBqSt04F_E1fNXwD1ShIg":3,"dVoGmm_swVnh9QAuz7e5kg":3,"kV768Ru9q3JKNNaKuKAKCw":5,"QgFlkWtQcmVS_hvF0w-nQQ":4,"yocrNUicnf88RPA6Iv3KWg":4,"jmgKs7CTqSWWwJnFnPIf4A":5,"zObyDUjiXSTCXa5t6w9ghg":3,"et-odMgalfrBGzhuMWoy3Q":3,"pQSkGB3HIunzNn_vIRWUNQ":3,"GjEV7-1f0z4DnrGneGyw7g":5,"aBUZtKoIzaIPgbPwR6-y4A":3,"r42_qusNI4WJoyME4pJRbA":3,"CsScv13bILZvI6L_l0oqxA":2,"ggoYlZeQhATwb_yGSntfdw":4,"nEY3mwbpAJlQ5FOQ-F4Giw":4,"yls6yVb_8tluUBmUa-lbdw":3,"jrJgVpJYhhQ9U1AZTBvnkA":3,"_v6HIliEOn0l0YaAmBOrxw":3,"76SwH7tNBaUzoBsRJ7bDNw":3,"HKnOkqBRJtRKeU5h7CEhdQ":2,"nLNA7OOkBKMLjn_WMHi_Zg":2,"xV3OGVeNZyARob-L1SSTPQ":4,"V3OnaQZcWH6wV-BZo_k8Zg":3},"xAFD6qLYBDxr8qwx68W7QQ":{"3ez4Qs56C_cC-l8x08l6Zw":3,"9OPheVf5o8sRcRHxJDl4-A":4,"HmNMIuTR3lH0OTpkog2dTQ":4,"G7Q0Tm2XBI5rqd5wyUc0jg":1,"-hQ8iZygzi0iiTFUkHgiEA":4,"e8FMAuTswDueAlLsNyLhcA":2,"5-X03Zc0nN7U5eoe8uFUdw":5,"TCqkBVN84Ek0oLmZGAX5xA":4,"me3myIgtuIgLEC5jd97uZw":5},"n5XTL82qlsnjoj9jUOfquA":{"E4KKFmUsWzgv-pPISdi1BQ":2,"vW4G1hwiW6LkuhAfbeRfqg":1,"yggyuN3FV_NiQCKfvN-b-Q":5,"aGbjLWzcrnEx2ZmMCFm3EA":3,"n25AWEdWRaNMdMI_uN_VOw":4,"JZWCBnrqU27DF8SOQq5yrw":2,"uJYw4p59AKh8c8h5yWMdOw":4,"IaUXrUfy2iYrR6dHgvTpUg":3,"ZqmBF2iLF1Czpl9bUM0NLg":2,"Xq9tkiHhyN_aBFswFeGLvA":3,"UpMR63WZgIn8VDKnYpDwXA":3,"2e2e7WgqU1BnpxmQL5jbfw":4,"M5z8jiXlONr5BWWIQU_zzA":4,"uFJwKlHL6HyHSJmORO8-5w":4,"f3EcPjqKftEznBSs2oQVRg":5,"J4qLz0nGzCTMf6-kf_SiQg":3,"yOVydU0J5-hKODrKGhH4yg":3,"NXsw4z0AtaILgS4-UxSWUg":3,"H3VRP8dk_qB_7NYtdU7x7w":2,"c2VrKERabMII-L5vUGi5iQ":3,"Es300Ys1XXPYg8aI7BKVYQ":4,"r-a-Cn9hxdEnYTtVTB5bMQ":4,"BQjGE1Z3nk253XzIZqt8Gg":4,"eq6lQI039SBLC6sHm3idGA":4,"Xhg93cMdemu5pAMkDoEdtQ":1,"sIyHTizqAiGu12XMLX3N3g":3,"wENkQMCxWrXy26--Y8Ggpw":4,"zt1TpTuJ6y9n551sw9TaEg":5,"Ht8mXLuqJSTPrU9kvzosUA":5,"DJlb6DLzT1yK5ipnL2I1dA":4},"xsavzkTWCziXDQwXeZt3iA":{"Lq6CDJ2yHmMs4N7jscQhHQ":2,"xqECECmAwrtFPUn-OXCAMw":4,"nLn4yNELpgpWADSHdIcCsg":4,"YppzR-sn8y15dmUd1lLcfw":2,"KwLfgeylp9d8zY3KacREiw":4,"UIqKaIBPgkIW3M7coOIZPQ":4,"nZgYNbl1XlZyyKlISMoG6w":4,"JauLZ0TL3D3VIGtSnStzhA":4,"vdFktqVjR1cjs0fA8hA-7w":4,"npfVfumxVAkQNYpY1fSvew":3,"4bPX-yR2hEYK1gdvw045YQ":5,"M-vOSYnyuaE2TsFJF0uMbQ":3,"aHUz8Npmmik5GxgooUoz_g":2,"HnhDu5WPH35KBjBn2PNwbg":5,"j_pce4pG9krrBeYwUni8Pg":4,"5uQ8X2wWTB0QnuQImLy2IQ":5,"snWpJGBxuw5HpyPRlGk-Lg":2,"1Fupq7erFi4uqC_gd9ypQg":3,"JyfJYQURfRuDvrWRlDDELw":4,"QvRK2dyv4EDxuJ-LuodE2Q":3,"NHBvlSKSP-AYgOgArRfIww":1,"l2lpBXx8jKl87J2szyJRuQ":5,"1jmSAp3ZTTUJ4idPrARfkw":3,"3fV9sL5LklD9ZSeONKmjkw":3,"-1tQu_yKCOgOj-WtXmMYIA":5,"Jlcx_J7DAqXthtsb_OMBEw":5,"Z6aaze-cgaYKKXlpuH9LqA":4,"1M7ScVRCiUYJVqjDbBx5pQ":4,"_j4jCjlnuUnsvq1UnfF1Ag":4,"jd8RFp00Uk5UVAoD046eDw":5,"xfwRO04KbAPw_zRotCfWQQ":1,"dOLatQ5cMzaKHkkN7sCMZA":4,"T4AyBSffvi3prLrw0H2enA":5,"l93r5g1WX4Gy6aB4_2yTkQ":5,"OVU0pQ85Zf74OVgDyPFvGQ":5,"wtD7EvFhxt8EeNODbl1G_A":4,"HN4UIInplQk3lTUsohQRhg":4,"tXydHtnQ2sU37kXy30CBLw":3,"KVvudcDpXPEx6SRTNSB9uQ":5,"pD7NzevYc6HhYu13wCxiiw":5,"5WYyDPDDcWfIIHssy6AmxQ":4,"6DqG808vLAu2v2NYn_YV_Q":4,"5tYLVPc2PKnj6E62sY6QMg":3,"0Y3VWMpXoRKbvy9mjQ7wdw":3,"PLgclJqCLffQfMov6wb8-g":2,"SBvw-IpLThBeiJF5qs9oMQ":4,"5tsqcZEvZYTpqux7_IGHVw":2,"KuQVzAzJZggFLi60OlBhmA":5,"scbkHTbGTOA4xOrRcU3bBw":4,"VAeiLMTICw2CSFpy28CsWQ":4,"kKcniirsMqUd_x0pZEGcWA":1,"gJp7Bg69fuOasm8oaMWBsQ":4,"33Am9frs0Bt48Zlwk1uVHQ":4,"yUVQl7y5e8IEDk4EAHr8zQ":5,"csgF8n0R5CIauWriNJl2vg":2,"amr-TqfnMpxmWf2RqnK_lA":2,"HsAYzU2-Z_vZAaRqHbcP8g":4,"8buIr1zBCO7OEcAQSZko7w":3,"NBFu9Ia-KzpsByWtoB6JhA":3,"XgfKcL7eBJE9B66qoaIlJQ":2,"6yoEpca0GnthoEzlJtNmgQ":3,"if4obdFN0d01nh62DzpwFA":3,"vha8-1iVade3hshLU0Co4Q":4,"JyOWfIFwzz1rq_NUdwXMRQ":4,"PXviRcHR1mqdH4vRc2LEAQ":4,"udGgvy4TYdsdv13j1UzOIg":4,"WOJU7788eEctbxdZwkqxWw":4,"7UStzgu75kpOKBoc2JnmVw":3,"Qher1XRFuU8GnhA4BH7wog":4,"xuPJkwww4b8X4j6n3c9KHA":5,"-GZsHVDlI6wvLsgD1Yaj0g":4,"1MMztCZKPtw9DoCVflfZFg":4,"nhToFLPoqNixNbRK4-xFQg":2,"_CHH9KN1bO5cs_GHjQ-r1A":5,"bzSzpGAn4kjGRtsgMM1pvg":4,"76cpjw4HcmTiDbWSTnf3XQ":5,"UZbkczu-KJour2Hgt_5WWw":4,"Cyqav-yBpo8O7VW6c4-ohA":4,"olwuTiAEEFgSYefWUcZWbQ":3,"Q_Rwcv9APBLggk2KAsBEvg":5,"9OFr3nlEDwncUNgbqFKd5w":3,"BUpMSaHWxlWTgKTDIzz5Lw":3,"xxZHUf4my1RMwGIp-sR_yA":2,"eq6lQI039SBLC6sHm3idGA":3,"3AMFoTdFm7j2bocSpm7Xxw":5,"xheJf3qJLLf4-Ck8ay3GFg":2,"R0MhNwopWTWXcg8CPAFgpw":4,"6zHlgXi4Ze_sPhUo5HnOSg":5,"EM4gmlsOVfXT4faEkp8IzQ":4,"wFN75sAjpPpYnf0De8QssA":1,"hCxNymBRhx7eQZdxGCjvXQ":1},"ENJpS6i-s9hWiQg9ZGwevQ":{"72INqF4dYTHdCoUoePIuSw":1,"sSiTG5DvIXRxFUiCo9H9DQ":5,"Xsl-i1otDd3GXJEkkKJCaw":5,"TqHTtjPANCBKGsjGBjDoQQ":1,"KFg2T3nHlzjMByX4y_V8LA":2,"_UrbZpgCq638dWrS0Vly2A":5,"Pr9rQKypHgC_J1AfufxzIw":3,"cN6aBxe2mQvrQlzk26LyRQ":5,"qkbloHdDZuHf_0wTqUGPjQ":5,"ykfTh6HI219NoMsWBxulxw":5,"XWvht_1ZLdK7EHJ3jo4q0g":4,"qbEJeRvytnBo5BGG1R5kGg":5,"5ZH0Gc2i1Sr9Uq-dwWRlzw":5,"TdNIQQcfslKjkey4-yAlKg":5,"ZdQbDVZWDsO-d7q2qW8E3A":5,"uKSX1n1RoAzGq4bV8GPHVg":2,"NVqLUZ7Vb9B_0RJm_BS64g":4,"PAtgWCLCFRQd_fjnihISOg":5,"FqzgT9Y-Yu7jiWdHnGW-kQ":3,"y-uHaMLLWQydSyWJawLIUw":1,"Um5VnQXli9IwplV2rmgggg":4,"pwpl-rxwNRQdgqFz_-qMPg":2,"Vu8od1U-h5qqwj3Jf_Hnzg":4},"fkOVvPXj9OfBqkGyOBwBUA":{"uYKwS-biARKgBkk5rY_PaQ":5,"1U1GRksKXF7q8FKcW0e5VQ":4,"QvRK2dyv4EDxuJ-LuodE2Q":4,"xV3OGVeNZyARob-L1SSTPQ":5,"oWVE6zUBws9eFhvvAfaK6g":4,"t65wgP7lQrCqxjBpMwOdbw":5},"bgDqBVENTrioOpQOozOYLg":{"0K634ehk41ZRc4kj3NTAEQ":1,"fUaHbVFnt4s5qoE8fAj6NA":5,"rXrCQcs7NOcOhpBFxjDkGQ":2,"53YGfwmbW73JhFiemNeyzQ":1,"IURIbkgQgHXAgwX6hAgiNQ":1},"--J9z98Cjl4t_ZnvmNy2mA":{"63d0v1xVzzahrY7zLoy_FA":3,"4UVhuOLaMm2-34SrW8y-ag":4,"zFcd_gelAUEwAvJOgiZpvg":5,"DqY2VlbRuQ3Mu2mlxd4xUQ":5,"YNQgak-ZLtYJQxlDwN-qIg":4,"qIDCkDsUcBGJhAZuX9e1VA":3,"mANSEm_FbXK6qtB7n6nWgg":2,"0L7nj_kFVMldRrZA7q6rvQ":4,"VK7XhT6wv-mWV6N1IU4xXA":1,"CZjcFdvJhksq9dy58NVEzw":4},"2uVAYBkbEqTZVK6BD80izQ":{"W-UBevF6tFgX4WiA8PvdPA":3,"2lL9IlU3p1Vt6skh5-Sc8w":3,"VAeiLMTICw2CSFpy28CsWQ":3,"dWW6PSpvxTXH0aDnYwU-fQ":1,"jSDLdzm7ZbMWL3g3D2GU9w":3,"1GYjuEYlbaQzEaCBKGirJg":5,"KwLfgeylp9d8zY3KacREiw":1,"R-HoFtiYyl4OIJqr09AdlQ":3,"A1dxN0YajU7qD8tqloeUfw":3,"k-ZTmIRDeZUvwiCGN51szA":5,"WnBSlcek6ACsjE0UDJ1l2A":3,"rKOSmt3oKFUaHHN0Y_YOHg":3,"6LNuxmnwiTvxXEDk06MkrA":4,"QIWX9XEgthrVKVC7U6xK3A":3,"cnugQPvKa5Mq0bHj145gjg":2,"GDXPlGpDGALcKNRpa5kMqw":2,"Wi8v4lZpgfUPRmNOXTIU6g":2,"deFBCKjvB6i3-LX12JlIuQ":5},"0y8aTKQGeCIUt7_zBu56Jw":{"tFU2Js_nbIZOrnKfYJYBBg":5,"3f-RP2-EE94eifGnepUBpg":5,"IVc23uY-36WUNYoIbz42Fg":4,"rP76z9iDOFczywAiee-l7A":5,"W4A_cYOAHhOQ-wb8E7suvg":5,"u9wjRhUjySkHPa_hG3kFOg":5,"fUdr6QMsrBGOYpxS6Dcjdg":5},"YJA1lVlA7NAknIQldUIcCQ":{"0lN71KKnrMMuRDIssDVGww":5,"Rp-v0BKc8JaN7pKj8P0pyg":4,"_eRCcfm68VqYwi8bTqAeiw":5,"CmCvsKSVNJwtiGggMw9Khw":5"}}
group2  = {"J-LDiDOvAp5PiE5PZx56Bg", "HeIv2xpid8OSu_YqFs8inw", "8Uq8gSxmvm6g5VBlEuSEUQ"}
# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs,person1,person2):
	# Get the list of shared_items
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1

	# if they have no ratings in common, return 0
	if len(si)==0: return 0

	# Add up the squares of all the differences
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])

	return 1/(1+sum_of_squares)

# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
	# Get the list of mutually rated items
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1

	# Find the number of elements
	n=len(si)

	# if they are no ratings in common, return 0
	if n==0: return 0

	# Add up all the preferences
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])

	# Sum up the squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

	# Sum up the products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

	# Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: return 0

	r=num/den

	return r

def transformPrefs(prefs): 
	result={}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			# Flip item and person
			result[item][person]=prefs[person][item]


	return result

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
	scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
	# Sort the list so the highest scores appear at the top
	scores.sort( )
	scores.reverse( )
	return scores[0:n]


# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		# don't compare me to myself
		if other==person: continue
		sim=similarity(prefs,person,other)

		# ignore scores of zero or lower
		if sim<=0: continue
		for item in prefs[other]:
			# only score movies I haven't seen yet
			if item not in prefs[person] or prefs[person][item]==0:
				# Similarity * Score
				totals.setdefault(item,0)
				totals[item]+=prefs[other][item]*sim
				# Sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+=sim



	# Create the normalized list
	rankings=[(total/simSums[item],item) for item,total in totals.items( )]

	# Return the sorted list
	rankings.sort( )
	rankings.reverse()
	return rankings


# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		# don't compare me to myself
		if other==person: continue
		sim=similarity(prefs,person,other)

		# ignore scores of zero or lower
		if sim<=0: continue
		for item in prefs[other]:
			# only score movies I haven't seen yet
			#if item not in prefs[person] or prefs[person][item]==0:
			# Similarity * Score
			totals.setdefault(item,0)
			totals[item]+=prefs[other][item]*sim
			# Sum of similarities
			simSums.setdefault(item,0)
			simSums[item]+=sim



	# Create the normalized list
	rankings=[(total/simSums[item],item) for item,total in totals.items( )]

	# Return the sorted list
	rankings.sort( )
	rankings.reverse()
	return rankings


def getGroupRecommendations(group):
	weightedRec={}
	for person in group:
		for score, movieName in getRecommendations(critics, person):
			if movieName in weightedRec.keys():
				weightedRec[movieName] += score 
			else:
				weightedRec[movieName] = score
	
	return weightedRec



			



def getRecommendedItems(prefs,itemMatch,user):
	userRatings=prefs[user]
	scores={}
	totalSim={}
	# Loop over items rated by this user
	for (item,rating) in userRatings.items( ):
		# Loop over items similar to this one
		for (similarity,item2) in itemMatch[item]:
			# Ignore if this user has already rated this item
			if item2 in userRatings: continue

			# Weighted sum of rating times similarity
			scores.setdefault(item2,0)
			scores[item2]+=similarity*rating

			# Sum of all the similarities
			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity

	# Divide each total score by total weighting to get an average
	rankings=[(score/totalSim[item],item) for item,score in scores.items( )]

	# Return the rankings from highest to lowest
	rankings.sort( )
	rankings.reverse( )

	return rankings



def calculateSimilarItems(prefs,n=10):
	# Create a dictionary of items showing which other items they
	# are most similar to.
	result={}
	# Invert the preference matrix to be item-centric
	itemPrefs=transformPrefs(prefs)
	c=0
	for item in itemPrefs:
		# Status updates for large datasets
		c+=1
		if c%100==0: print "%d / %d" % (c,len(itemPrefs))
		# Find the most similar items to this one
		scores=topMatches(itemPrefs,item,n=n,similarity=sim_pearson)
		result[item]=scores

	return result

def groupSimilarItems(group):
	weightedRec={}
	for person in group:
		for score, movieName in getRecommendedItems(critics,itemsim,person):
			if movieName in weightedRec.keys():
				weightedRec[movieName] += score 
			else:
				weightedRec[movieName] = score
	
	return weightedRec

def getHighestRecommendation(recommendations):
	highest = 0
	index = 0
	for rec in recommendations.keys():
		if recommendations[rec] > highest:
			highest = recommendations[rec]
			index = rec
	return index

itemsim = calculateSimilarItems(yelpDict)

similarItems = groupSimilarItems(group2)

output = getHighestRecommendation(similarItems)



#rec = getGroupRecommendations(group1)
#output = getHighestRecommendation(rec)
print output




