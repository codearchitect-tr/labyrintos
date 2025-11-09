# LabyrinthOS - A Self-Solving Maze

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg) ![Concept](https://img.shields.io/badge/Concept-Procedural%20Generation-purple.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

**LabyrinthOS**, her çalıştırıldığında prosedürel olarak benzersiz bir labirent oluşturan ve ardından bu labirenti gözlerinizin önünde canlı olarak çözen bir simülasyondur.

Bu proje, bir problemin çözümünü (yol bulma) ve bir dünyanın yaratılışını (labirent oluşturma) görsel ve dinamik bir şekilde sergiler.

## Süreç

1.  **Yaratılış (Creation):** Program, `Recursive Backtracking` algoritmasını kullanarak boş bir alandan rastgele bir labirent "oyar".
2.  **Keşif (Exploration):** Bir "gezgin" (`☺`), `Depth-First Search` (DFS) algoritmasını kullanarak labirentin içinde yolunu aramaya başlar. Gittiği yolları işaretler (`·`).
3.  **Çözüm (Solution):** Gezgin çıkışa ulaştığında, geri dönerek sadece doğru yolu (`●`) vurgular ve çözüm haritasını ortaya çıkarır.

Bu, bir algoritmanın düşünme sürecini canlı izlemek gibidir.

## Nasıl Çalışır?

Tek yapmanız gereken script'i çalıştırmak:
```bash
python labyrintos.py
