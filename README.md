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

[link](readme/images/final_score_per_game_for_strategy_crawdadstrategy.png)





Clearly, the threshold strategy captures a range of performance that tends to optimize around 300. Investigating this further, we look at scores for threshold strategy in the threshold range of [200,400]:

| Strategy | E[Num_Turns_to_Win] | Std[Num_Turns_to_Win] | E[Final_Score] | Std[Final_Score] | E[Score_Per_Turn] | Std[Score_Per_Turn] | E[Rolls_Per_Turn] | Std[Rolls_Per_Turn] |
| --- | ----------- | --- | ----------- |  --- | ----------- |  --- | ----------- |  --- |
|CrawdadStrategy|[409.229](readme/images/number_of_turns_to_win_per_game_for_strategy_crawdadstrategy.png)|145.99534650186698|[10718.75](readme/images/final_score_per_game_for_strategy_crawdadstrategy.png)|676.8338359904457|[22.05](readme/images/histogram_of_scores_per_turn_(crawdadstrategy).png)|177.40566583474802|[3.875](readme/images/histogram_of_num_rolls_per_turn_(crawdadstrategy).png)|2.3881118227750724|
|TylerStrategy|[29.16](readme/images/number_of_turns_to_win_per_game_for_strategy_tylerstrategy.png)|5.474702948322618|[10347.3](readme/images/final_score_per_game_for_strategy_tylerstrategy.png)|416.5407737739683|[348.35](readme/images/histogram_of_scores_per_turn_(tylerstrategy).png)|348.498534758367|[1.01](readme/images/histogram_of_num_rolls_per_turn_(tylerstrategy).png)|0.09954853042566682|
|ThresholdStrategy:210|[24.0143](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-210.png)|4.039495916909222|[10348.295](readme/images/final_score_per_game_for_strategy_thresholdstrategy-210.png)|390.9752282919134|[433.445](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-210).png)|363.4080193306848|[1.6362](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-210).png)|0.7195146490051563|
|ThresholdStrategy:220|[24.065](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-220.png)|4.12580625184009|[10355.615](readme/images/final_score_per_game_for_strategy_thresholdstrategy-220.png)|398.1131386705521|[429.88](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-220).png)|366.470484025066|[1.6343](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-220).png)|0.7213983307127592|
|ThresholdStrategy:230|[24.1117](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-230.png)|4.076749329859496|[10343.24](readme/images/final_score_per_game_for_strategy_thresholdstrategy-230.png)|381.6266058421879|[434.925](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-230).png)|370.64367261320524|[1.6281](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-230).png)|0.7178035345353345|
|ThresholdStrategy:240|[24.1056](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-240.png)|4.052862100925828|[10346.085](readme/images/final_score_per_game_for_strategy_thresholdstrategy-240.png)|387.0812653249916|[426.42](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-240).png)|369.4639819568294|[1.6479](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-240).png)|0.7252435369024546|
|ThresholdStrategy:250|[24.0296](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-250.png)|4.116967182511683|[10348.91](readme/images/final_score_per_game_for_strategy_thresholdstrategy-250.png)|385.0670585287144|[425.46](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-250).png)|357.6312044660544|[1.6231](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-250).png)|0.7175638506697356|
|ThresholdStrategy:260|[24.241](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-260.png)|4.285038524391065|[10350.915](readme/images/final_score_per_game_for_strategy_thresholdstrategy-260.png)|378.92119352457735|[425.285](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-260).png)|380.5067638225784|[1.842](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-260).png)|0.8471763516394196|
|ThresholdStrategy:270|[24.2006](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-270.png)|4.261076779117194|[10368.62](readme/images/final_score_per_game_for_strategy_thresholdstrategy-270.png)|412.94230557642487|[425.9](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-270).png)|373.12680466730893|[1.8395](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-270).png)|0.8491241671187545|
|ThresholdStrategy:280|[24.1855](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-280.png)|4.292147714513134|[10357.105](readme/images/final_score_per_game_for_strategy_thresholdstrategy-280.png)|397.2701238831496|[420.565](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-280).png)|368.89556675150874|[1.8452](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-280).png)|0.8454043002274618|
|ThresholdStrategy:290|[24.3012](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-290.png)|4.333884725702977|[10351.175](readme/images/final_score_per_game_for_strategy_thresholdstrategy-290.png)|385.31898012769193|[428.78](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-290).png)|380.2343611733974|[1.837](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-290).png)|0.8394649904236714|
|ThresholdStrategy:300|[24.2969](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-300.png)|4.296905482981091|[10352.4](readme/images/final_score_per_game_for_strategy_thresholdstrategy-300.png)|376.2830037217852|[427.795](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-300).png)|371.5629070216609|[1.8404](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-300).png)|0.8548689490746574|
|ThresholdStrategy:310|[25.3806](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-310.png)|4.803774689254952|[10372.87](readme/images/final_score_per_game_for_strategy_thresholdstrategy-310.png)|392.8102507436751|[407.985](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-310).png)|400.4273017382777|[2.0567](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-310).png)|0.9895367746086197|
|ThresholdStrategy:320|[25.3908](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-320.png)|4.77878217079452|[10372.595](readme/images/final_score_per_game_for_strategy_thresholdstrategy-320.png)|402.68092972987534|[412.49](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-320).png)|401.02877990018476|[2.0428](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-320).png)|0.9955236143490885|
|ThresholdStrategy:330|[25.3429](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-330.png)|4.773991902995751|[10375.465](readme/images/final_score_per_game_for_strategy_thresholdstrategy-330.png)|388.2375002632552|[405.975](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-330).png)|386.55205551666967|[2.0654](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-330).png)|0.985301944579528|
|ThresholdStrategy:340|[25.3718](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-340.png)|4.819697885632551|[10367.265](readme/images/final_score_per_game_for_strategy_thresholdstrategy-340.png)|380.7245262542054|[406.74](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-340).png)|394.79255124160034|[2.0576](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-340).png)|0.9824351163694158|
|ThresholdStrategy:350|[25.3435](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-350.png)|4.808910511959149|[10373.25](readme/images/final_score_per_game_for_strategy_thresholdstrategy-350.png)|387.3473135238315|[411.525](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-350).png)|405.1812453201109|[2.0519](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-350).png)|0.986257400664774|
|ThresholdStrategy:360|[26.9097](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-360.png)|5.493392726390917|[10396.135](readme/images/final_score_per_game_for_strategy_thresholdstrategy-360.png)|412.93869231565253|[378.43](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-360).png)|406.4151232732888|[2.2345](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-360).png)|1.1181389777113344|
|ThresholdStrategy:370|[27.0458](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-370.png)|5.526586349245577|[10395.37](readme/images/final_score_per_game_for_strategy_thresholdstrategy-370.png)|399.58106762328003|[380.375](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-370).png)|412.5871207250886|[2.2296](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-370).png)|1.1117587151644346|
|ThresholdStrategy:380|[26.9355](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-380.png)|5.5208502722653945|[10401.225](readme/images/final_score_per_game_for_strategy_thresholdstrategy-380.png)|405.8961992276532|[382.265](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-380).png)|413.67660389277614|[2.2351](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-380).png)|1.1246130292000642|
|ThresholdStrategy:390|[26.9792](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-390.png)|5.536861298904311|[10396.23](readme/images/final_score_per_game_for_strategy_thresholdstrategy-390.png)|390.5291774039942|[387.88](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-390).png)|424.33608344232425|[2.2436](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-390).png)|1.1241821109330348|
|ThresholdStrategy:400|[26.9464](readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-400.png)|5.577171104041221|[10394.85](readme/images/final_score_per_game_for_strategy_thresholdstrategy-400.png)|407.8248516348178|[388.59](readme/images/histogram_of_scores_per_turn_(thresholdstrategy-400).png)|419.2742431739623|[2.2324](readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-400).png)|1.1317766262974258|

The raw output for this is below:

<details>
  <summary>Click to expand!</summary>

  ```json
  {
    "CrawdadStrategy": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 1000,
                "minmax": [
                    50,
                    958
                ],
                "mean": 409.229,
                "variance": 21314.6412002002,
                "skewness": 0.5383189587666654,
                "kurtosis": 0.33118091606083766
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_crawdadstrategy.png",
            "finalScoresStats": {
                "nobs": 1000,
                "minmax": [
                    10000,
                    17700
                ],
                "mean": 10718.75,
                "variance": 458104.0415415415,
                "skewness": 2.727036006207771,
                "kurtosis": 15.663463408546821
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_crawdadstrategy.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 1000,
                "minmax": [
                    0,
                    2150
                ],
                "mean": 22.05,
                "variance": 31472.770270270277,
                "skewness": 8.888656845175511,
                "kurtosis": 85.12971759320546
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(crawdadstrategy).png",
            "rollsPerTurnStats": {
                "nobs": 1000,
                "minmax": [
                    1,
                    18
                ],
                "mean": 3.875,
                "variance": 5.703078078078078,
                "skewness": 1.9966090733240813,
                "kurtosis": 5.276383569356758
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(crawdadstrategy).png"
        }
    },
    "TylerStrategy": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 1000,
                "minmax": [
                    13,
                    51
                ],
                "mean": 29.16,
                "variance": 29.972372372372373,
                "skewness": 0.17815358911499513,
                "kurtosis": 0.0270595047111013
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_tylerstrategy.png",
            "finalScoresStats": {
                "nobs": 1000,
                "minmax": [
                    10000,
                    13400
                ],
                "mean": 10347.3,
                "variance": 173506.2162162162,
                "skewness": 2.72883551377366,
                "kurtosis": 11.558474655120923
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_tylerstrategy.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 1000,
                "minmax": [
                    0,
                    2400
                ],
                "mean": 348.35,
                "variance": 121451.22872872873,
                "skewness": 2.1161018581014384,
                "kurtosis": 5.832881435009339
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(tylerstrategy).png",
            "rollsPerTurnStats": {
                "nobs": 1000,
                "minmax": [
                    1,
                    2
                ],
                "mean": 1.01,
                "variance": 0.009909909909909911,
                "skewness": 9.864173018495201,
                "kurtosis": 95.49289150015176
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(tylerstrategy).png"
        }
    },
    "ThresholdStrategy:210": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    9,
                    39
                ],
                "mean": 24.0143,
                "variance": 16.317527262726273,
                "skewness": 0.05029144287971943,
                "kurtosis": 0.017174434623926427
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-210.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17700
                ],
                "mean": 10348.295,
                "variance": 152861.6291379138,
                "skewness": 3.0839952663446164,
                "kurtosis": 22.03993759728522
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-210.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4100
                ],
                "mean": 433.445,
                "variance": 132065.3885138514,
                "skewness": 2.165563286738794,
                "kurtosis": 9.407158151760584
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-210).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6362,
                "variance": 0.5177013301330132,
                "skewness": 0.8789680050156637,
                "kurtosis": 0.22252489609869786
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-210).png"
        }
    },
    "ThresholdStrategy:220": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    8,
                    39
                ],
                "mean": 24.065,
                "variance": 17.02227722772277,
                "skewness": 0.08213573862626021,
                "kurtosis": 0.10421312970848673
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-220.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17000
                ],
                "mean": 10355.615,
                "variance": 158494.0711821182,
                "skewness": 3.062096313445673,
                "kurtosis": 19.168381980424158
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-220.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 429.88,
                "variance": 134300.61566156617,
                "skewness": 2.315604716833924,
                "kurtosis": 10.80074387283078
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-220).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6343,
                "variance": 0.5204155515551555,
                "skewness": 0.9088336113543455,
                "kurtosis": 0.32016895131443857
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-220).png"
        }
    },
    "ThresholdStrategy:230": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    8,
                    41
                ],
                "mean": 24.1117,
                "variance": 16.619885098509847,
                "skewness": 0.05509340626540323,
                "kurtosis": 0.09616587740213056
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-230.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17700
                ],
                "mean": 10343.24,
                "variance": 145638.86628662868,
                "skewness": 3.186153387992411,
                "kurtosis": 24.53204055165881
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-230.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    5000
                ],
                "mean": 434.925,
                "variance": 137376.73204820487,
                "skewness": 2.355769470127566,
                "kurtosis": 11.312682163041696
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-230).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6281,
                "variance": 0.5152419141914192,
                "skewness": 0.9394256145303008,
                "kurtosis": 0.5180305481188614
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-230).png"
        }
    },
    "ThresholdStrategy:240": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    4,
                    39
                ],
                "mean": 24.1056,
                "variance": 16.425691209120913,
                "skewness": 0.0641294337584813,
                "kurtosis": 0.03594587925392867
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-240.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17400
                ],
                "mean": 10346.085,
                "variance": 149831.90596559655,
                "skewness": 3.4389029029716434,
                "kurtosis": 28.715650652048634
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-240.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    8000
                ],
                "mean": 426.42,
                "variance": 136503.63396339637,
                "skewness": 3.2255996870391863,
                "kurtosis": 29.9583467562439
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-240).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6479,
                "variance": 0.5259781878187819,
                "skewness": 0.8760678480085413,
                "kurtosis": 0.2626887075250295
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-240).png"
        }
    },
    "ThresholdStrategy:250": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    7,
                    43
                ],
                "mean": 24.0296,
                "variance": 16.949418781878187,
                "skewness": 0.034903121129216376,
                "kurtosis": 0.12976621220377726
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-250.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    14600
                ],
                "mean": 10348.91,
                "variance": 148276.63956395639,
                "skewness": 2.6903060158071828,
                "kurtosis": 12.612532717885165
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-250.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    5000
                ],
                "mean": 425.46,
                "variance": 127900.07840784079,
                "skewness": 2.420751918613237,
                "kurtosis": 13.419349583999782
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-250).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.6231,
                "variance": 0.5148978797879786,
                "skewness": 0.9231526028292566,
                "kurtosis": 0.3522432005581755
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-250).png"
        }
    },
    "ThresholdStrategy:260": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    7,
                    42
                ],
                "mean": 24.241,
                "variance": 18.361555155515553,
                "skewness": 0.12764033982590647,
                "kurtosis": 0.14228102213135907
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-260.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16300
                ],
                "mean": 10350.915,
                "variance": 143581.2709020902,
                "skewness": 3.0484894148117223,
                "kurtosis": 18.65307894542243
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-260.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4100
                ],
                "mean": 425.285,
                "variance": 144785.39731473147,
                "skewness": 2.1844362451647705,
                "kurtosis": 10.583501524251634
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-260).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 1.842,
                "variance": 0.7177077707770776,
                "skewness": 0.7562874567772394,
                "kurtosis": 0.05036266727879557
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-260).png"
        }
    },
    "ThresholdStrategy:270": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    9,
                    43
                ],
                "mean": 24.2006,
                "variance": 18.156775317531757,
                "skewness": 0.10859343723402062,
                "kurtosis": 0.10403073637748639
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-270.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17150
                ],
                "mean": 10368.62,
                "variance": 170521.34773477347,
                "skewness": 3.603607469900953,
                "kurtosis": 28.567545322840928
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-270.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 425.9,
                "variance": 139223.61236123613,
                "skewness": 2.040553170375145,
                "kurtosis": 9.694605273571936
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-270).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.8395,
                "variance": 0.7210118511851185,
                "skewness": 0.7675368028307199,
                "kurtosis": 0.027809261813774633
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-270).png"
        }
    },
    "ThresholdStrategy:280": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    43
                ],
                "mean": 24.1855,
                "variance": 18.42253200320032,
                "skewness": 0.11744690979659538,
                "kurtosis": 0.17139728732573012
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-280.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16900
                ],
                "mean": 10357.105,
                "variance": 157823.55133013302,
                "skewness": 3.373164811203993,
                "kurtosis": 24.051396022522244
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-280.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4100
                ],
                "mean": 420.565,
                "variance": 136083.93916891684,
                "skewness": 1.9278101335185545,
                "kurtosis": 8.166328803425113
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-280).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 1.8452,
                "variance": 0.7147084308430843,
                "skewness": 0.7711239564436734,
                "kurtosis": 0.11339040002318423
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-280).png"
        }
    },
    "ThresholdStrategy:290": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    44
                ],
                "mean": 24.3012,
                "variance": 18.78255681568157,
                "skewness": 0.12504579172705704,
                "kurtosis": 0.12677567272977797
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-290.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17700
                ],
                "mean": 10351.175,
                "variance": 148470.71644664466,
                "skewness": 3.3138955455090264,
                "kurtosis": 24.978080088998745
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-290.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 428.78,
                "variance": 144578.16941694164,
                "skewness": 2.0406532969158153,
                "kurtosis": 8.92526279410481
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-290).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 1.837,
                "variance": 0.7047014701470148,
                "skewness": 0.7414595813270815,
                "kurtosis": -0.04504057490091551
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-290).png"
        }
    },
    "ThresholdStrategy:300": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    5,
                    42
                ],
                "mean": 24.2969,
                "variance": 18.463396729672965,
                "skewness": 0.0970074806696016,
                "kurtosis": 0.1172835135324779
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-300.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    14350
                ],
                "mean": 10352.4,
                "variance": 141588.89888988898,
                "skewness": 2.710317680597878,
                "kurtosis": 12.905009998386832
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-300.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 427.795,
                "variance": 138058.99387438744,
                "skewness": 1.8341850109747058,
                "kurtosis": 7.180642818948819
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-300).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    5
                ],
                "mean": 1.8404,
                "variance": 0.7308009200920091,
                "skewness": 0.8097615028288072,
                "kurtosis": 0.15283174975502822
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-300).png"
        }
    },
    "ThresholdStrategy:310": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    46
                ],
                "mean": 25.3806,
                "variance": 23.076251265126512,
                "skewness": 0.21140650454612606,
                "kurtosis": 0.23194487890356497
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-310.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16000
                ],
                "mean": 10372.87,
                "variance": 154299.89308930893,
                "skewness": 3.069375665806407,
                "kurtosis": 19.828929014772655
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-310.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4800
                ],
                "mean": 407.985,
                "variance": 160342.0239773977,
                "skewness": 1.9254544858925242,
                "kurtosis": 8.946756854412406
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-310).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.0567,
                "variance": 0.9791830283028302,
                "skewness": 0.6513986712432507,
                "kurtosis": -0.2297701383334192
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-310).png"
        }
    },
    "ThresholdStrategy:320": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    49
                ],
                "mean": 25.3908,
                "variance": 22.83675903590359,
                "skewness": 0.21178509896421888,
                "kurtosis": 0.1824485551100321
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-320.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17800
                ],
                "mean": 10372.595,
                "variance": 162151.9311681168,
                "skewness": 3.7751129578916016,
                "kurtosis": 33.61296807140411
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-320.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 412.49,
                "variance": 160824.08230823083,
                "skewness": 1.932369510513325,
                "kurtosis": 9.312761022647726
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-320).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    7
                ],
                "mean": 2.0428,
                "variance": 0.9910672667266727,
                "skewness": 0.7075500288844719,
                "kurtosis": -0.08785997433563697
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-320).png"
        }
    },
    "ThresholdStrategy:330": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    9,
                    47
                ],
                "mean": 25.3429,
                "variance": 22.790998689868985,
                "skewness": 0.24478516240930484,
                "kurtosis": 0.09390415943245012
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-330.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    14900
                ],
                "mean": 10375.465,
                "variance": 150728.35661066105,
                "skewness": 2.8250221010790773,
                "kurtosis": 15.280439643578305
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-330.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4000
                ],
                "mean": 405.975,
                "variance": 149422.49162416247,
                "skewness": 1.5669531822541474,
                "kurtosis": 5.731480505252009
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-330).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.0654,
                "variance": 0.9708199219921992,
                "skewness": 0.6055488516244188,
                "kurtosis": -0.3692340470159108
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-330).png"
        }
    },
    "ThresholdStrategy:340": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    9,
                    45
                ],
                "mean": 25.3718,
                "variance": 23.22948770877088,
                "skewness": 0.2305302926595931,
                "kurtosis": 0.10424033014612233
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-340.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    13950
                ],
                "mean": 10367.265,
                "variance": 144951.16489148914,
                "skewness": 2.6659976366075395,
                "kurtosis": 12.637171696620168
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-340.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 406.74,
                "variance": 155861.15851585162,
                "skewness": 1.80323929075067,
                "kurtosis": 7.621237114435965
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-340).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.0576,
                "variance": 0.9651787578757877,
                "skewness": 0.6334177444433929,
                "kurtosis": -0.25948242339052197
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-340).png"
        }
    },
    "ThresholdStrategy:350": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    49
                ],
                "mean": 25.3435,
                "variance": 23.125620312031202,
                "skewness": 0.222958847145518,
                "kurtosis": 0.33213290205998725
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-350.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    14300
                ],
                "mean": 10373.25,
                "variance": 150037.9412941294,
                "skewness": 2.716714660668586,
                "kurtosis": 12.974192519992851
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-350.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    8000
                ],
                "mean": 411.525,
                "variance": 164171.8415591559,
                "skewness": 2.4479659347428626,
                "kurtosis": 20.261297957040252
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-350).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.0519,
                "variance": 0.9727036603660365,
                "skewness": 0.6680845152002525,
                "kurtosis": -0.19753014186486517
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-350).png"
        }
    },
    "ThresholdStrategy:360": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    6,
                    50
                ],
                "mean": 26.9097,
                "variance": 30.17736364636464,
                "skewness": 0.2875901017994657,
                "kurtosis": 0.2141851645261399
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-360.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17950
                ],
                "mean": 10396.135,
                "variance": 170518.36361136113,
                "skewness": 3.4681437264710273,
                "kurtosis": 27.783274833647194
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-360.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4000
                ],
                "mean": 378.43,
                "variance": 165173.25242524254,
                "skewness": 1.4196986102034663,
                "kurtosis": 4.11670887086591
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-360).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    7
                ],
                "mean": 2.2345,
                "variance": 1.2502347734773478,
                "skewness": 0.5575264164452074,
                "kurtosis": -0.5015500495885354
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-360).png"
        }
    },
    "ThresholdStrategy:370": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    8,
                    50
                ],
                "mean": 27.0458,
                "variance": 30.54315667566756,
                "skewness": 0.2883949780105509,
                "kurtosis": 0.15673290728797173
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-370.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    15750
                ],
                "mean": 10395.37,
                "variance": 159665.02960296028,
                "skewness": 2.8063471018135373,
                "kurtosis": 15.559807789888623
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-370.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4800
                ],
                "mean": 380.375,
                "variance": 170228.13218821882,
                "skewness": 1.8238850935862132,
                "kurtosis": 8.686666274885992
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-370).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.2296,
                "variance": 1.2360074407440744,
                "skewness": 0.574654174303613,
                "kurtosis": -0.4214459609254333
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-370).png"
        }
    },
    "ThresholdStrategy:380": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    5,
                    53
                ],
                "mean": 26.9355,
                "variance": 30.47978772877288,
                "skewness": 0.27000697765500553,
                "kurtosis": 0.23278626604467423
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-380.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    17600
                ],
                "mean": 10401.225,
                "variance": 164751.72454745474,
                "skewness": 3.0162406127160275,
                "kurtosis": 20.68938386376144
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-380.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 382.265,
                "variance": 171128.33260826083,
                "skewness": 1.6450460104192477,
                "kurtosis": 6.431706597483618
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-380).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.2351,
                "variance": 1.2647544654465444,
                "skewness": 0.5838275228520273,
                "kurtosis": -0.4069631488058114
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-380).png"
        }
    },
    "ThresholdStrategy:390": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    5,
                    53
                ],
                "mean": 26.9792,
                "variance": 30.656833043304335,
                "skewness": 0.31957956646195684,
                "kurtosis": 0.37100850697271737
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-390.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    14400
                ],
                "mean": 10396.23,
                "variance": 152513.0384038404,
                "skewness": 2.662818549681746,
                "kurtosis": 13.260009081091908
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-390.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4800
                ],
                "mean": 387.88,
                "variance": 180061.11171117116,
                "skewness": 1.7108981195954285,
                "kurtosis": 6.730357137943276
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-390).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    6
                ],
                "mean": 2.2436,
                "variance": 1.2637854185418542,
                "skewness": 0.5452814096531514,
                "kurtosis": -0.5063937407305485
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-390).png"
        }
    },
    "ThresholdStrategy:400": {
        "simulateGames": {
            "numTurnsStats": {
                "nobs": 10000,
                "minmax": [
                    9,
                    54
                ],
                "mean": 26.9464,
                "variance": 31.104837523752373,
                "skewness": 0.3131285788360232,
                "kurtosis": 0.18505906972898378
            },
            "numTurnsStatsHistogram": "readme/images/number_of_turns_to_win_per_game_for_strategy_thresholdstrategy-400.png",
            "finalScoresStats": {
                "nobs": 10000,
                "minmax": [
                    10000,
                    16600
                ],
                "mean": 10394.85,
                "variance": 166321.1096109611,
                "skewness": 3.2963637527380594,
                "kurtosis": 22.309069794444472
            },
            "finalScoresStatsHistogram": "readme/images/final_score_per_game_for_strategy_thresholdstrategy-400.png"
        },
        "simulateTurns": {
            "scoresPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    0,
                    4050
                ],
                "mean": 388.59,
                "variance": 175790.89098909887,
                "skewness": 1.6817179753134253,
                "kurtosis": 6.446243338366882
            },
            "scoresPerTurnStatsHistogram": "readme/images/histogram_of_scores_per_turn_(thresholdstrategy-400).png",
            "rollsPerTurnStats": {
                "nobs": 10000,
                "minmax": [
                    1,
                    7
                ],
                "mean": 2.2324,
                "variance": 1.2809183318331832,
                "skewness": 0.5726167549927422,
                "kurtosis": -0.47140200528047105
            },
            "rollsPerTurnStatsHistogram": "readme/images/histogram_of_num_rolls_per_turn_(thresholdstrategy-400).png"
        }
    }
}
 ```
</details>

