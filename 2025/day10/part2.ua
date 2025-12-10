&fras "input"
⊜{⊜(⊢□) ⊸≠ @ } ⊸≠ @\n
≡(⊢°□)
ParseLights   ← ≠@# ↘¯⟜↘ 1
ParseNumsLike ← ⊜⋕⊸≠@,↘¯⟜↘ 1
⍚⊃{◇ParseLights⊢|⍚ParseNumsLike↘¯⟜↘ 1|◇ParseNumsLike⊣}
≡°□
≡↘₁
Calculator ← (
  ⊙(⇡⊸⧻)
  ≡⌞◇(≡◇∊)
  ⊃(⍚⊚
    ⍚($"_==_"/◇($"_+_")⍚$"buttons[_]")
  | $"buttons = [ Int('button%s' % i) for i in range(_) ]"⧻⍉)
  &p "o = Optimize()"
  ⊙&p
  &p "o.add(*[i >= 0 for i in buttons])"
  &p "presses = Int('presses')"
  /$"_,_"
  &p $"o.add(_)"
  &p $"o.add(sum(buttons)==presses)"
  &p "o.minimize(presses)"
  &p "o.check()"
  &p "print(o.model()[presses])"
)
&p "from z3 import*"
≡(Calculator∩°□◇°⊟)
