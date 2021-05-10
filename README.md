# DiceGame



## Results

The table below captures the results of 10,000 simulations for each strategy:

| Strategy | E[Num_Turns_to_Win] | Std[Num_Turns_to_Win] | E[Final_Score] | Std[Final_Score] | E[Score_Per_Turn] | Std[Score_Per_Turn] | E[Rolls_Per_Turn] | Std[Rolls_Per_Turn] |
| --- | ----------- | --- | ----------- |  --- | ----------- |  --- | ----------- |  --- |
|CrawdadStrategy|394.094|149.23204537688065|10701.75|583.4765482711215|33.1|217.74251261938218|3.922|2.49482266707278|
|TylerStrategy|29.086|5.60946254734534|10359.8|493.5509624674563|357.25|356.71021807579285|1.014|0.1334983963267792|
|ThresholdStrategy:100|27.707|5.039751076103949|10345.285|415.2616801503603|372.95|356.5263084273867|1.0911|0.28845989480531103|
|ThresholdStrategy:200|24.7387|4.184444200527321|10339.4|392.7213554243016|417.14|358.32884387952305|1.4038|0.5919295549808321|
|ThresholdStrategy:300|24.2084|4.28961647714013|10355.06|384.65594031451263|427.715|373.7727911244189|1.8504|0.8570258393589618|
|ThresholdStrategy:400|26.9955|5.543839208104482|10394.04|391.76884343024045|386.25|423.0500379783263|2.2436|1.131188312660571|
|ThresholdStrategy:500|27.8791|6.575241940085329|10458.535|423.50128584091794|375.81|471.76434801710695|2.5107|1.2925372626185776|
|ThresholdStrategy:600|27.8231|7.030088804905703|10497.2|440.2766679650824|374.175|495.25129657546177|2.6871|1.3262614700535844|
|ThresholdStrategy:700|29.0773|7.68463597530861|10536.24|461.1349335527447|369.75|530.3881301998242|2.851|1.393267066757817|
|ThresholdStrategy:800|31.7709|9.20387333237653|10587.49|473.27306984431726|341.935|553.4056663589159|3.0229|1.4940544869183947|
|ThresholdStrategy:900|33.4708|10.08230691118184|10616.35|483.87146088508456|313.385|557.6066573252415|3.1285|1.550815350976796|
|ThresholdStrategy:1000|34.9728|11.056187592855363|10667.92|512.442809846461|304.88|570.4969169708345|3.2455|1.6763981570850368|

The raw output for this is below:

<details>
  <summary>Click to expand!</summary>
  
  ## Heading
  ```
  
  ```
</details>

Clearly, the threshold strategy captures a range of performance that tends to optimize around 300. Investigating this further, we look at scores for threshold strategy in the threshold range of [200,400]:

| Strategy | E[Num_Turns_to_Win] | Std[Num_Turns_to_Win] | E[Final_Score] | Std[Final_Score] | E[Score_Per_Turn] | Std[Score_Per_Turn] | E[Rolls_Per_Turn] | Std[Rolls_Per_Turn] |
| --- | ----------- | --- | ----------- |  --- | ----------- |  --- | ----------- |  --- |
|CrawdadStrategy|403.412|144.46090546998937|10702.35|646.9741517657819|34.45|231.78529272135006|3.846|2.2718814769801363|
|TylerStrategy|28.681|5.322928946789782|10345.7|393.9183693123255|378.55|423.8006660029034|1.017|0.1293357171384909|
|ThresholdStrategy:210|24.0485|4.0566480484926135|10341.33|383.09072939800444|427.75|372.56719948462074|1.6327|0.7169673034465527|
|ThresholdStrategy:220|24.0835|4.052575734888702|10340.435|367.31628455636167|428.09|366.45720212338415|1.638|0.7180581875837609|
|ThresholdStrategy:230|24.0599|4.134927055242355|10349.56|404.3620373696405|435.925|374.73015176746105|1.6173|0.7077363909535159|
|ThresholdStrategy:240|24.0208|4.081351872028474|10352.495|390.86929126664006|431.705|367.58135777057305|1.6215|0.7153243452391992|
|ThresholdStrategy:250|24.0435|4.10722469308266|10348.36|391.7175700239479|429.205|381.43592818680725|1.6153|0.7079237427877104|
|ThresholdStrategy:260|24.2867|4.233898404493187|10362.9|402.34721115950686|431.345|386.22488001266066|1.8527|0.8510435579415141|
|ThresholdStrategy:270|24.3016|4.286825763605602|10355.38|391.69426602875353|430.37|381.537311638085|1.8487|0.861093756942776|
|ThresholdStrategy:280|24.274|4.292338106049157|10356.71|385.4988156060708|423.915|368.72878768396527|1.8436|0.8508886185301308|
|ThresholdStrategy:290|24.2547|4.224998576484627|10353.88|388.5042331222601|431.935|385.18208979550167|1.8326|0.8461966939692499|
|ThresholdStrategy:300|24.2946|4.273153030688507|10353.115|384.330349773181|425.16|385.1704947565469|1.8525|0.8611724053818602|
|ThresholdStrategy:310|25.3414|4.827315645121392|10374.055|405.93975622445305|407.01|386.5369335265363|2.0432|0.9743863211633704|
|ThresholdStrategy:320|25.3733|4.804670185929473|10368.675|394.49595318673175|405.21|395.9987845988171|2.0611|0.9961255024351401|
|ThresholdStrategy:330|25.3179|4.76899506409811|10382.075|411.0515061510794|410.07|389.6168312939301|2.0634|0.9852296725894806|
|ThresholdStrategy:340|25.5061|4.842324607124152|10373.26|393.51297011123347|407.235|395.6950369049669|2.0578|0.9924503291175718|
|ThresholdStrategy:350|25.3569|4.840440618015848|10370.435|400.5636102987758|404.295|404.21175352674857|2.068|0.9930128939045787|
|ThresholdStrategy:360|26.9796|5.5335021283614285|10395.025|403.8190267380124|389.155|424.64593297456554|2.2263|1.115622145386657|
|ThresholdStrategy:370|27.0364|5.634061528323106|10395.21|396.7320197936549|387.155|417.8172005749758|2.229|1.130525014619698|
|ThresholdStrategy:380|26.9295|5.588063385041326|10402.05|401.4740535097681|385.015|434.221780465309|2.2359|1.1261340984983894|
|ThresholdStrategy:390|26.9761|5.511367008885424|10393.165|396.5617970769374|385.125|412.41240618375855|2.237|1.1234577053550223|
|ThresholdStrategy:400|26.9864|5.5257097631742|10392.03|396.1264579866784|380.98|412.6333314537529|2.2372|1.1203846152855799|

The raw output for this is below:

<details>
  <summary>Click to expand!</summary>
  ```yaml
  {
    "CrawdadStrategy": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 1000,
                "minmax": [
                    89,
                    969
                ],
                "mean": 403.412,
                "variance": 20868.953209209205,
                "skewness": 0.5007081131661607,
                "kurtosis": 0.18272386957238762
            },
            "finalScoresStats": {
                "nobs": 1000,
                "minmax": [
                    10000,
                    18250
                ],
                "mean": 10702.35,
                "variance": 418575.55305305304,
                "skewness": 3.012929126743015,
                "kurtosis": 21.80109009541371
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 1000,
                "minmax": [
                    0,
                    3550
                ],
                "mean": 34.45,
                "variance": 53724.42192192194,
                "skewness": 8.343473186333812,
                "kurtosis": 85.08228966995188
            },
            "rollsPerTurnStats": {
                "nobs": 1000,
                "minmax": [
                    1,
                    18
                ],
                "mean": 3.846,
                "variance": 5.1614454454454455,
                "skewness": 1.8583343070658498,
                "kurtosis": 4.570199797393859
            }
        }
    },
    "TylerStrategy": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 1000,
                "minmax": [
                    12,
                    45
                ],
                "mean": 28.681,
                "variance": 28.333572572572574,
                "skewness": 0.13474888345082872,
                "kurtosis": -0.039946938390199804
            },
            "finalScoresStats": {
                "nobs": 1000,
                "minmax": [
                    10000,
                    13750
                ],
                "mean": 10345.7,
                "variance": 155171.6816816817,
                "skewness": 2.2814425870474473,
                "kurtosis": 8.782565061155843
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 1000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 378.55,
                "variance": 179607.00450450453,
                "skewness": 3.375191481107269,
                "kurtosis": 19.119971567842022
            },
            "rollsPerTurnStats": {
                "nobs": 1000,
                "minmax": [
                    1,
                    2
                ],
                "mean": 1.017,
                "variance": 0.016727727727727727,
                "skewness": 7.483902306019882,
                "kurtosis": 54.117023986696275
            }
        }
    },
    "ThresholdStrategy:210": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    41
                ],
                "mean": 24.0485,
                "variance": 16.45639338933893,
                "skewness": 0.04654665734949312,
                "kurtosis": 0.09953938571396126
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16550
                ],
                "mean": 10341.33,
                "variance": 146758.50695069507,
                "skewness": 3.2090582400083214,
                "kurtosis": 20.815514245249137
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 427.75,
                "variance": 138806.31813181317,
                "skewness": 2.404192669240335,
                "kurtosis": 11.785718671091054
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6327,
                "variance": 0.5140421142114211,
                "skewness": 0.883231495213508,
                "kurtosis": 0.22249518179996297
            }
        }
    },
    "ThresholdStrategy:220": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    5,
                    41
                ],
                "mean": 24.0835,
                "variance": 16.4233700870087,
                "skewness": 0.02512399693297164,
                "kurtosis": 0.23214247732229865
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    14450
                ],
                "mean": 10340.435,
                "variance": 134921.25290029004,
                "skewness": 2.591332605508794,
                "kurtosis": 11.902095560921044
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 428.09,
                "variance": 134290.88098809883,
                "skewness": 2.4487125217265096,
                "kurtosis": 12.119411240786835
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.638,
                "variance": 0.5156075607560756,
                "skewness": 0.8687108377549451,
                "kurtosis": 0.19576454084126027
            }
        }
    },
    "ThresholdStrategy:230": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    2,
                    41
                ],
                "mean": 24.0599,
                "variance": 17.097621752175215,
                "skewness": 0.03831486800345149,
                "kurtosis": 0.17153033998783318
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16800
                ],
                "mean": 10349.56,
                "variance": 163508.65726572656,
                "skewness": 3.5433780000663204,
                "kurtosis": 24.821853099358815
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4000
                ],
                "mean": 435.925,
                "variance": 140422.68664366438,
                "skewness": 2.317521164853588,
                "kurtosis": 10.481601561213004
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6173,
                "variance": 0.500890799079908,
                "skewness": 0.9124498073932252,
                "kurtosis": 0.36043449211069456
            }
        }
    },
    "ThresholdStrategy:240": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    40
                ],
                "mean": 24.0208,
                "variance": 16.65743310331033,
                "skewness": 0.04268806774541244,
                "kurtosis": 0.16700279995718148
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    13950
                ],
                "mean": 10352.495,
                "variance": 152778.80285528552,
                "skewness": 2.7612344836550484,
                "kurtosis": 12.919219547935072
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4000
                ],
                "mean": 431.705,
                "variance": 135116.05458045803,
                "skewness": 2.2291357724727545,
                "kurtosis": 9.78288295406543
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6215,
                "variance": 0.511688918891889,
                "skewness": 0.9294251309040645,
                "kurtosis": 0.38494749343184687
            }
        }
    },
    "ThresholdStrategy:250": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    5,
                    40
                ],
                "mean": 24.0435,
                "variance": 16.86929467946795,
                "skewness": 0.046427281093971894,
                "kurtosis": 0.1486541235522041
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17150
                ],
                "mean": 10348.36,
                "variance": 153442.65466546654,
                "skewness": 3.262600553251363,
                "kurtosis": 22.99730568959016
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    8000
                ],
                "mean": 429.205,
                "variance": 145493.36731173118,
                "skewness": 3.8161383524796135,
                "kurtosis": 43.14430458117469
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6153,
                "variance": 0.5011560256025603,
                "skewness": 0.9365214915481627,
                "kurtosis": 0.4788797362341688
            }
        }
    },
    "ThresholdStrategy:260": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    7,
                    44
                ],
                "mean": 24.2867,
                "variance": 17.92589569956996,
                "skewness": 0.12738299242953324,
                "kurtosis": 0.21302230569953062
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16500
                ],
                "mean": 10362.9,
                "variance": 161883.27832783278,
                "skewness": 3.2827030719593346,
                "kurtosis": 20.845246574672583
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    5000
                ],
                "mean": 431.345,
                "variance": 149169.65794079413,
                "skewness": 2.114551831824568,
                "kurtosis": 10.163811589059177
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.8527,
                "variance": 0.7242751375137513,
                "skewness": 0.736315587174272,
                "kurtosis": -0.07442037865641193
            }
        }
    },
    "ThresholdStrategy:270": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    5,
                    42
                ],
                "mean": 24.3016,
                "variance": 18.376875127512754,
                "skewness": 0.14714820471777743,
                "kurtosis": 0.21148203514827157
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17250
                ],
                "mean": 10355.38,
                "variance": 153424.39803980396,
                "skewness": 3.435760712165243,
                "kurtosis": 27.237074451943933
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 430.37,
                "variance": 145570.7201720172,
                "skewness": 2.0787338145141385,
                "kurtosis": 9.435716973650365
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 1.8487,
                "variance": 0.7414824582458246,
                "skewness": 0.7985167321565692,
                "kurtosis": 0.11298998749495892
            }
        }
    },
    "ThresholdStrategy:280": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    45
                ],
                "mean": 24.274,
                "variance": 18.424166416641665,
                "skewness": 0.1448471994743714,
                "kurtosis": 0.2629221472456784
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    15200
                ],
                "mean": 10356.71,
                "variance": 148609.3368336834,
                "skewness": 2.819216963681702,
                "kurtosis": 14.573812059575353
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 423.915,
                "variance": 135960.91886688673,
                "skewness": 1.756309725748372,
                "kurtosis": 6.434054166668931
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 1.8436,
                "variance": 0.7240114411441144,
                "skewness": 0.8074744205839318,
                "kurtosis": 0.19455512441409395
            }
        }
    },
    "ThresholdStrategy:290": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    42
                ],
                "mean": 24.2547,
                "variance": 17.850612971297128,
                "skewness": 0.07691751602919705,
                "kurtosis": 0.16399460083720685
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17650
                ],
                "mean": 10353.88,
                "variance": 150935.53915391542,
                "skewness": 3.2453883863695334,
                "kurtosis": 24.011787607821315
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4100
                ],
                "mean": 431.935,
                "variance": 148365.24229922993,
                "skewness": 2.23623114486687,
                "kurtosis": 11.562079097064775
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.8326,
                "variance": 0.7160488448844884,
                "skewness": 0.7855806229168428,
                "kurtosis": 0.06616828434200128
            }
        }
    },
    "ThresholdStrategy:300": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    5,
                    48
                ],
                "mean": 24.2946,
                "variance": 18.259836823682367,
                "skewness": 0.14177284045899752,
                "kurtosis": 0.16348444241754834
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17300
                ],
                "mean": 10353.115,
                "variance": 147709.81775677568,
                "skewness": 3.2586041260210683,
                "kurtosis": 23.67498458698417
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 425.16,
                "variance": 148356.3100310031,
                "skewness": 2.3455786516570307,
                "kurtosis": 12.388391862079876
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 1.8525,
                "variance": 0.741617911791179,
                "skewness": 0.8001044997248038,
                "kurtosis": 0.19812654220712034
            }
        }
    },
    "ThresholdStrategy:310": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    7,
                    46
                ],
                "mean": 25.3414,
                "variance": 23.302976337633762,
                "skewness": 0.23193637466304864,
                "kurtosis": 0.2025972506325866
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16650
                ],
                "mean": 10374.055,
                "variance": 164787.08568356835,
                "skewness": 3.377086751070034,
                "kurtosis": 22.405625018997682
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 407.01,
                "variance": 149410.80098009796,
                "skewness": 1.595722932960974,
                "kurtosis": 5.85698275292466
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.0432,
                "variance": 0.9494287028702869,
                "skewness": 0.6622664179454053,
                "kurtosis": -0.150573495423437
            }
        }
    },
    "ThresholdStrategy:320": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    5,
                    48
                ],
                "mean": 25.3733,
                "variance": 23.08485559555956,
                "skewness": 0.2783227049223853,
                "kurtosis": 0.40481294689264935
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17350
                ],
                "mean": 10368.675,
                "variance": 155627.05708070807,
                "skewness": 3.6162696409432384,
                "kurtosis": 31.033263006241555
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4800
                ],
                "mean": 405.21,
                "variance": 156815.03740374034,
                "skewness": 1.7716216691800626,
                "kurtosis": 7.392055370410713
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    7
                ],
                "mean": 2.0611,
                "variance": 0.9922660166016603,
                "skewness": 0.6438535029938856,
                "kurtosis": -0.2545181744240912
            }
        }
    },
    "ThresholdStrategy:330": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    8,
                    45
                ],
                "mean": 25.3179,
                "variance": 22.74331392139214,
                "skewness": 0.22536562709020175,
                "kurtosis": 0.17415408579009117
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16950
                ],
                "mean": 10382.075,
                "variance": 168963.34070907088,
                "skewness": 3.6876562644959274,
                "kurtosis": 29.36505095546036
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 410.07,
                "variance": 151801.27522752277,
                "skewness": 1.6232615709435296,
                "kurtosis": 5.865790064521896
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    7
                ],
                "mean": 2.0634,
                "variance": 0.970677507750775,
                "skewness": 0.665591231702596,
                "kurtosis": -0.12162217803086905
            }
        }
    },
    "ThresholdStrategy:340": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    4,
                    46
                ],
                "mean": 25.5061,
                "variance": 23.44810760076008,
                "skewness": 0.20607095498152495,
                "kurtosis": 0.2161284556012446
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17550
                ],
                "mean": 10373.26,
                "variance": 154852.45764576455,
                "skewness": 3.3153792873746206,
                "kurtosis": 25.450437874100942
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 407.235,
                "variance": 156574.56223122313,
                "skewness": 1.8168380691826012,
                "kurtosis": 7.8714394556102025
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.0578,
                "variance": 0.9849576557655767,
                "skewness": 0.659039768622151,
                "kurtosis": -0.23199837326982475
            }
        }
    },
    "ThresholdStrategy:350": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    7,
                    46
                ],
                "mean": 25.3569,
                "variance": 23.429865376537652,
                "skewness": 0.2570188750012829,
                "kurtosis": 0.2282389212582654
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17600
                ],
                "mean": 10370.435,
                "variance": 160451.20589558955,
                "skewness": 3.947563034177669,
                "kurtosis": 37.161724026973204
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    8000
                ],
                "mean": 404.295,
                "variance": 163387.14168916893,
                "skewness": 2.53964056797265,
                "kurtosis": 21.31248259821431
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.068,
                "variance": 0.986074607460746,
                "skewness": 0.6666180622087644,
                "kurtosis": -0.1372201785680205
            }
        }
    },
    "ThresholdStrategy:360": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    7,
                    51
                ],
                "mean": 26.9796,
                "variance": 30.619645804580458,
                "skewness": 0.3100613898473553,
                "kurtosis": 0.12509343656313998
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17650
                ],
                "mean": 10395.025,
                "variance": 163069.80635563558,
                "skewness": 3.2835672750171025,
                "kurtosis": 24.644329662934815
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 389.155,
                "variance": 180324.1683918392,
                "skewness": 1.6673877509986854,
                "kurtosis": 6.006241676775778
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    7
                ],
                "mean": 2.2263,
                "variance": 1.2446127712771275,
                "skewness": 0.5674137953512096,
                "kurtosis": -0.418095140957802
            }
        }
    },
    "ThresholdStrategy:370": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    52
                ],
                "mean": 27.0364,
                "variance": 31.742649304930495,
                "skewness": 0.3397976815691571,
                "kurtosis": 0.2627119946462133
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    14250
                ],
                "mean": 10395.21,
                "variance": 157396.29552955297,
                "skewness": 2.670194661041882,
                "kurtosis": 12.546986874494621
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 387.155,
                "variance": 174571.21309630957,
                "skewness": 1.638189327610724,
                "kurtosis": 5.760113025594784
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.229,
                "variance": 1.278086808680868,
                "skewness": 0.5796104418577619,
                "kurtosis": -0.48734152632377636
            }
        }
    },
    "ThresholdStrategy:380": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    53
                ],
                "mean": 26.9295,
                "variance": 31.226452395239523,
                "skewness": 0.30790326470344903,
                "kurtosis": 0.115622638708341
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    15000
                ],
                "mean": 10402.05,
                "variance": 161181.41564156415,
                "skewness": 2.531292938137352,
                "kurtosis": 11.499102364036672
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    8000
                ],
                "mean": 385.015,
                "variance": 188548.554630463,
                "skewness": 2.612116757085196,
                "kurtosis": 24.289180494721702
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.2359,
                "variance": 1.26817800780078,
                "skewness": 0.5503726751346137,
                "kurtosis": -0.5191437511923445
            }
        }
    },
    "ThresholdStrategy:390": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    53
                ],
                "mean": 26.9761,
                "variance": 30.375166306630664,
                "skewness": 0.3151558162488039,
                "kurtosis": 0.2706030061022262
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17100
                ],
                "mean": 10393.165,
                "variance": 157261.2589008901,
                "skewness": 3.1999961170424287,
                "kurtosis": 24.257606029100476
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4000
                ],
                "mean": 385.125,
                "variance": 170083.99277427743,
                "skewness": 1.4923974778468219,
                "kurtosis": 4.436791636976571
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    8
                ],
                "mean": 2.237,
                "variance": 1.2621572157215724,
                "skewness": 0.5753455583294035,
                "kurtosis": -0.3828455680503331
            }
        }
    },
    "ThresholdStrategy:400": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    52
                ],
                "mean": 26.9864,
                "variance": 30.53346838683868,
                "skewness": 0.2609630769907243,
                "kurtosis": 0.11824143698019673
            },
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16650
                ],
                "mean": 10392.03,
                "variance": 156916.1707170717,
                "skewness": 2.9329875295438725,
                "kurtosis": 17.648557455686895
            }
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 380.98,
                "variance": 170266.26622662268,
                "skewness": 1.769600516006514,
                "kurtosis": 7.479998191695913
            },
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    7
                ],
                "mean": 2.2372,
                "variance": 1.2552616861686168,
                "skewness": 0.5737736281466055,
                "kurtosis": -0.41943259020471757
            }
        }
    }
}
  ```
</details>
