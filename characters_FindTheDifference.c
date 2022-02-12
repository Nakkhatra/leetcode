#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char findTheDifference(char *s, char *t)
{
    if (strlen(s) == 0)
    {
        return t[0];
    }

    char different_character = '\0';

    char *s_ptr = (char *)malloc((strlen(s) + 1) * sizeof(char));
    char *t_ptr = (char *)malloc((strlen(t) + 1) * sizeof(char));
    s_ptr[strlen(s)] = '\0';
    t_ptr[strlen(t)] = '\0';

    for (size_t i = 0; i < strlen(t); i++)
    {
        if (i != (strlen(t) - 1))
        {
            if ((s[i] >= 65) && (s[i] <= 90))
            {
                s_ptr[i] = s[i] + 32;
            }
            else
            {
                s_ptr[i] = s[i];
            }
        }
        if ((t[i] >= 65) && (t[i] <= 90))
        {
            t_ptr[i] = t[i] + 32;
        }
        else
        {
            t_ptr[i] = t[i];
        }
    }

    int different_character_estimator[26];
    for (size_t i = 0; i < 26; i++)
    {
        different_character_estimator[i] = 0;
    }

    for (size_t i = 0; i < strlen(t); i++)
    {
        if (i != strlen(t) - 1)
        {
            different_character_estimator[s_ptr[i] - 'a']--;
        }
        different_character_estimator[t_ptr[i] - 'a']++;
    }

    for (size_t i = 0; i < 26; i++)
    {
        if (different_character_estimator[i] == 1)
        {
            different_character = 'a' + i;
            break;
        }
    }
    return different_character;
}

int main(void)
{
    char *s = "Nakshatra";
    char *t = "aNshagtark";
    char diff_char = findTheDifference(s, t);
    printf("\n\nThe different character in string 't' is: %c\n\n", diff_char);
    return 0;
}
