import openai

if __name__ == '__main__':
    history = """ 
    1. e4 e5 2. Nf3 Nc6 3. c3 Bc5 4. d4 exd4 5. cxd4 Bb4+ 6. Bd2 Bxd2+ 7. Qxd2 Nge7
8. Nc3 Ng6 9. Bd3 d6 10. O-O-O O-O 11. h3 Qf6 12. Bc2 Qf4 13. d5 Qxd2+ 14. Rxd2
Nce5 15. Nxe5 dxe5 16. Ne2 b6 17. g3 Ba6 18. Bd3 Bxd3 19. Rxd3 Rac8 20. f4 exf4
21. gxf4 Rfd8 22. Rf3 c6 23. dxc6 Rxc6+ 24. Kb1 Rd2 25. Nc3 Nh4 26. Rg3 Ng2 27.
Rg1 Nxf4 28. Rxg7+ Kf8 29. Rg8+ Ke7 30. Nd5+ Nxd5 31. exd5 Rxd5 32. Re1+ Re6 33.
Rf1 Rde5 34. Kc2 Re2+ 35. Kb3 a5 36. Rg7 R6e3+ 37. Ka4 Re4+ 38. Kb5 Rxb2+ 39.
Ka6 Kd6 40. Rfxf7 Rbb4 41. Rd7+ Kc5 42. Rc7+ Kd6 43. Rgd7+ Ke5 44. Re7+ Kf4 45.
Rf7+ Ke3 46. Rc3+ Kd2 47. Rff3 Red4 48. Rce3 Kc2 49. Rc3+ Kd2 50. a3 Ra4 51. Rb3
Rd6 52. Rxb6 Rxb6+ 53. Kxb6 Kc2 54. Rf7 Kb3 55. Rxh7 Rxa3 56. h4 a4 57. h5 Kb2
58. h6 Rb3+ 59. Kc5 a3 60. Ra7 a2 61. h7 Rc3+ 62. Kd4 Rh3 63. Ke4 Rxh7 64. Rxa2+
Kxa2 65. Ke5 Kb3 66. Kf6 Rh5 67. Ke7 Ra5 68. Kf6 Kc4 69. Ke7 Kd5 70. Kf6 Kd6 71.
Kf7 Rf5+ 72. Kg6 Ke6 73. Kg7 Rf6 74. Kh8 Kf7 75. Kh7 Rf1 76. Kh6 Kf6 77. Kh5 Kf5
78. Kh4 Kf4 79. Kh3 Rg1 80. Kh2 Rg8 81. Kh3 Kf3 82. Kh4 Kf4 83. Kh5 Kf5 84. Kh6
Kf6 85. Kh7 Kf7 86. Kh6 Rg6+ 87. Kh5 Kf6 88. Kh4 Rg5 89. Kh3 Kf5 90. Kh4 Rg8 91.
Kh3 Kf4 92. Kh4 Rh8# 0-1
    """

    openai.api_key = "INSERT_KEY"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="explain this game: " + history,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=1,
        presence_penalty=1
    )
    ai_response = response["choices"][0]["text"]
    print(ai_response)
