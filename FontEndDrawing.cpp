#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>
#include <fstream>
using namespace sf;
using namespace std;
void Export(vector<RectangleShape> rects) {
    ofstream file("Images/output.txt");
    for (int i = 0; i < rects.size(); ++i) {
        if (rects.at(i).getFillColor() == Color::Black) {
            file << "1";
        }
        else if(rects.at(i).getFillColor() == Color::White) {
            file << "0";
        }
        else if(rects.at(i).getFillColor() == Color(200,200,200)) {
            file << "2";
        }
    }
    file.close();
    return;
}
int main()
{
    
    sf::RenderWindow window(sf::VideoMode(1200, 980), "SFML works!");
    vector<RectangleShape> rects;

    RectangleShape clear;
    clear.setFillColor(Color::Black);
    clear.setOutlineColor(Color::Red);
    clear.setOutlineThickness(2);
    clear.setPosition(Vector2f(1050, 390));
    clear.setSize({ 100,80 });

    RectangleShape end;
    end.setFillColor(Color::Black);
    end.setOutlineColor(Color::Cyan);
    end.setOutlineThickness(2);
    end.setPosition(Vector2f(1050, 490));
    end.setSize({ 100,80 });

    for (int i = 0; i < 28; ++i) {
        for (int j = 0; j < 28; ++j) {
            RectangleShape temp;
            temp.setSize({ 35,35 });
            temp.setFillColor(Color::White);
            temp.setPosition(Vector2f( j * 35,i * 35));
            temp.setOutlineColor(Color::Black);
            temp.setOutlineThickness(2);
            rects.push_back(temp);
        }
    }

    while (window.isOpen())
    {
        
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }

       
        for (int i = 0; i < 28 * 28; ++i) {
            window.draw(rects.at(i));
        }
        window.draw(end);
        window.draw(clear);
        window.display();
        while (!Mouse::isButtonPressed(Mouse::Button::Left)) {
            //wait
        }
        if (Mouse::isButtonPressed(Mouse::Button::Left)) {
            if(Mouse::getPosition(window).x > 0 && Mouse::getPosition(window).y > 0 && Mouse::getPosition(window).x < 980 && Mouse::getPosition(window).y < 980) {
                end.setFillColor(Color::Black);
                int x = Mouse::getPosition(window).x;
                int y = Mouse::getPosition(window).y;

                x = x / 35;
                y = y / 35;

                int pos = y * 28 + x;

                rects.at(pos).setFillColor(Color::Black);
                if (pos + 1 < rects.size()) {
                    if(rects.at(pos+1).getFillColor() == Color::White)
                    rects.at(pos + 1).setFillColor(Color(200,200,200));
                }
                if (pos - 1 < rects.size()) {
                    if (rects.at(pos - 1).getFillColor() == Color::White)
                    rects.at(pos - 1).setFillColor(Color(200,200,200));
                }
                if (pos + 28 < rects.size()) {
                    if (rects.at(pos + 28).getFillColor() == Color::White)
                    rects.at(pos + 28).setFillColor(Color(200,200,200));
                }
                if (pos - 28 < rects.size()) {
                    if (rects.at(pos -28).getFillColor() == Color::White)
                    rects.at(pos -28).setFillColor(Color(200,200,200));
                }
                
                
                
            }
            if (Mouse::getPosition(window).x >= 1050 && Mouse::getPosition(window).y > 490 && Mouse::getPosition(window).x <= 1150 && Mouse::getPosition(window).y <= 570) {
                cout << "y";
                Export(rects);
                end.setFillColor(Color::Cyan);
            }
            if (Mouse::getPosition(window).x >= 1050 && Mouse::getPosition(window).y > 390 && Mouse::getPosition(window).x <= 1150 && Mouse::getPosition(window).y <= 470) {
                for (int i = 0; i < 28 * 28; ++i) {
                    rects.at(i).setFillColor(Color::White);
                }
                
            }

        }
        
        window.clear();
        
    }

    return 0;
}